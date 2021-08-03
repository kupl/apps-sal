class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        res = []
        i = 0
        letters = collections.Counter(letters)
        res = [0]
        self.dfs(i, words, letters, score, 0, res)
        return res[0]

    def dfs(self, i, words, letters, score, current, res):
        res[0] = max(res[0], current)

        for index in range(i, len(words)):
            word = words[index]
            cnt = collections.Counter(word)
            temp = 0
            valid = True
            for ch in cnt:
                if cnt[ch] > letters[ch]:
                    valid = False
                    break
                temp += cnt[ch] * score[ord(ch) - ord('a')]

            if not valid:
                continue
            else:
                for ch in cnt:
                    letters[ch] -= cnt[ch]
                self.dfs(index + 1, words, letters, score, current + temp, res)
                for ch in cnt:
                    letters[ch] += cnt[ch]
        return
