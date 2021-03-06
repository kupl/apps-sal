class Solution:

    def largestMultipleOfThree(self, a: List[int]) -> str:
        (n, dp) = (len(a), [''] * 3)
        a.sort(reverse=True)
        for i in range(n):
            (d, dp1) = (a[i] % 3, [''] * 3)
            for j in range(3):
                k = (j - d) % 3
                dp1[j] = max([dp[k] + str(a[i]) if dp[k] or k == 0 else '', dp[j]], key=lambda x: (len(x), x))
                if len(dp1[j]) >= 2 and dp1[j][0] == '0':
                    dp1[j] = dp1[j][1:]
            dp = dp1
        return dp[0]
