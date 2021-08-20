class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def is_predecessor(x, y):
            if len(x) != len(y) - 1:
                return False
            i = 0
            j = 0
            while i < len(x) and j < len(y):
                if x[i] == y[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            if i == len(x):
                return True
            return False
        words = sorted(words, key=lambda x: len(x))
        n = len(words)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if is_predecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
