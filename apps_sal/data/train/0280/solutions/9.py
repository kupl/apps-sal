class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # dp[i][k]: min change number of devide s[:i] to k substrings

        dp = [[2 ** 30 for _ in range(k + 1)] for _ in range(len(s) + 1)]
        for p in range(k + 1):
            dp[0][p] = 0

        def minChange(s: str) -> int:
            i, j = 0, len(s) - 1
            cnt = 0
            while i < j:
                if s[i] != s[j]:
                    cnt += 1
                i += 1
                j -= 1
            return cnt

        for i in range(1, len(s) + 1):
            for p in range(1, min(i, k) + 1):
                for j in range(i, p - 1, -1):
                    dp[i][p] = min(dp[i][p], dp[j - 1][p - 1] + minChange(s[j - 1:i]))

        return dp[-1][-1]
