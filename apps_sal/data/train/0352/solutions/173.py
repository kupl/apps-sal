import collections


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def chain(w1, w2):
            m, n = len(w1), len(w2)
            if abs(m - n) != 1:
                return False
            i, j, one = 0, 0, 1
            while i < m and j < n:
                if w1[i] == w2[j]:
                    i, j = i + 1, j + 1
                elif one:
                    one, i = 0, i + 1
                else:
                    return False
            return True

        if not words:
            return 0
        words.sort(key=lambda x: len(x))
        n = len(words)
        dp = [1] * n
        ans = 1
        for i in range(n):
            for j in range(i):
                if chain(words[i], words[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans
