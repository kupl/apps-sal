class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def getCount(i: int, j: int):
            count = 0
            while i < j:
                if s[i] != s[j]:
                    count += 1
                i += 1
                j -= 1
            return count

        INT_MAX = 2147483647
        N = len(s)
        dp = [[INT_MAX for x in range(k)] for y in range(N)]

        for i in range(N):
            dp[i][0] = getCount(0, i)

        for i in range(1, k):
            for j in range(i, N):
                for x in range(i - 1, j):
                    dp[j][i] = min(dp[j][i], dp[x][i - 1] + getCount(x + 1, j))
        return dp[N - 1][k - 1]
