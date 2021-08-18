class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        if not words:
            return 0

        words.sort(key=lambda x: len(x))
        n = len(words)
        dp = [1 for i in range(n)]

        for i in range(1, n):
            for j in range(i):
                if self.is_predecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def is_predecessor(self, word1, word2):

        if len(word1) + 1 != len(word2):
            return False

        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            if word1[i] == word2[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == len(word1)
