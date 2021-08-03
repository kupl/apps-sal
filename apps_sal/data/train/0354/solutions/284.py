class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[] for i in range(6)]
        for i in range(6):
            dp[i] = [0] * rollMax[i]
            dp[i][0] = 1

        # print(dp)

        total = 6
        for i in range(1, n):
            for j in range(6):
                tmpSum = sum(dp[j])
                for k in reversed(range(1, min(rollMax[j], n))):
                    dp[j][k] = dp[j][k - 1]
                dp[j][0] = total - tmpSum

            # print(dp)
            newTotal = 0
            for j in range(6):
                newTotal += sum(dp[j])
            total = newTotal

        m = pow(10, 9) + 7
        return total % m
