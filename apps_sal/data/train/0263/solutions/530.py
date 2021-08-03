class Solution:
    def knightDialer(self, N: int) -> int:

        dp = [0] * 10

        for j in range(10):
            dp[j] = 1

        for i in range(1, N):
            tmp0 = (dp[4] + dp[6]) % (math.pow(10, 9) + 7)
            tmp1 = (dp[6] + dp[8]) % (math.pow(10, 9) + 7)
            tmp2 = (dp[7] + dp[9]) % (math.pow(10, 9) + 7)
            tmp3 = (dp[4] + dp[8]) % (math.pow(10, 9) + 7)
            tmp4 = (dp[0] + dp[3] + dp[9]) % (math.pow(10, 9) + 7)
            tmp5 = 0
            tmp6 = (dp[0] + dp[1] + dp[7]) % (math.pow(10, 9) + 7)
            tmp7 = (dp[2] + dp[6]) % (math.pow(10, 9) + 7)
            tmp8 = (dp[1] + dp[3]) % (math.pow(10, 9) + 7)
            tmp9 = (dp[2] + dp[4]) % (math.pow(10, 9) + 7)

            dp[0] = tmp0
            dp[1] = tmp1
            dp[2] = tmp2
            dp[3] = tmp3
            dp[4] = tmp4
            dp[5] = tmp5
            dp[6] = tmp6
            dp[7] = tmp7
            dp[8] = tmp8
            dp[9] = tmp9

        total = 0
        for j in range(10):
            if N > 1 and j == 5:
                continue
            total += dp[j]

        total = int(total % (math.pow(10, 9) + 7))
        return total
