class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        if n == 0 or m == 0:
            return max(n, m)

        DeleteT1 = 0
        DeleteT2 = 1
        Match = 2

        dp = [[(0, None) for j in range(m + 1)] for i in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = (i, DeleteT1)
        for j in range(1, m + 1):
            dp[0][j] = (j, DeleteT2)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = (dp[i - 1][j - 1][0], Match)
                    continue

                val = min(dp[i - 1][j][0], dp[i][j - 1][0])
                if val == dp[i - 1][j][0]:
                    dp[i][j] = (val + 1, DeleteT1)
                else:
                    dp[i][j] = (val + 1, DeleteT2)

        i, j = n, m
        T1Length = n
        while i >= 0 and j >= 0:
            comb = dp[i][j]
            if comb[1] == DeleteT1:
                i -= 1
                T1Length -= 1
            elif comb[1] == DeleteT2:
                j -= 1
            else:
                i -= 1
                j -= 1

        return T1Length
