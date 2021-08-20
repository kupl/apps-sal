class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        m = len(letters)
        letters = collections.Counter(letters)
        ans = 0
        for i in range(1, n + 1):
            combinations = list(itertools.combinations(words, i))
            for combine in combinations:
                tempScore = self.calculateScore(''.join(combine), letters, score)
                ans = max(tempScore, ans)
        return ans

    def calculateScore(self, s, letters, score):
        counter = collections.Counter(s)
        ans = 0
        for ch in counter:
            if counter[ch] > letters[ch]:
                return float('-inf')
            ans += counter[ch] * score[ord(ch) - ord('a')]
        return ans
