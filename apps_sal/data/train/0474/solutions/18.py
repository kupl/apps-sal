class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        lettersCounter = collections.Counter(letters)
        scoreDict = {letter: score for (letter, score) in zip('abcdefghijklmnopqrstuvwxyz', score)}
        self.cache = [{} for i in range(len(words))]
        return self.backtracking(words, 0, lettersCounter, scoreDict)

    def backtracking(self, words, cur, remainLC, scoreDict):
        if cur >= len(words):
            return 0
        signature = tuple(((key, remainLC[key]) for key in sorted(remainLC)))
        if signature in self.cache[cur]:
            return self.cache[cur][signature]
        notChoose = self.backtracking(words, cur + 1, remainLC, scoreDict)
        wc = collections.Counter(words[cur])
        if any((remainLC[w] < wc[w] for w in wc.keys())):
            return notChoose
        diff = remainLC - wc
        curScore = sum((scoreDict[ch] for ch in words[cur]))
        choose = self.backtracking(words, cur + 1, diff, scoreDict)
        ans = max(curScore + choose, notChoose)
        self.cache[cur][signature] = ans
        return ans
