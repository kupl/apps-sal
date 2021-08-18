class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        dp = [[0 for _ in range(len(rollMax))] for _ in range(n + 1)]
        sums_dict = {}
        sums_dict[0] = 1
        for j in range(len(rollMax)):
            dp[1][j] = 1

        for i in range(2, n + 1):
            sums_dict[i - 1] = sum(dp[i - 1])
            for j in range(len(rollMax)):
                steps = rollMax[j]
                k = 1
                ans = 0
                while k <= min(steps, i):
                    row_sum = sums_dict[i - k]
                    ans += row_sum - dp[i - k][j]
                    k += 1
                dp[i][j] = ans

        return sum(dp[n]) % (10**9 + 7)
