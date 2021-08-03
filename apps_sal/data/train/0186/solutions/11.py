class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0] * (target + 1)

        for t in range(1, target + 1):
            for d, c in zip(range(1, len(cost) + 1), cost):
                if t == c:
                    dp[t] = max(dp[t], d)
                if c < t and dp[t - c] != 0:
                    dp[t] = max(dp[t], dp[t - c] * 10 + d)
        # print(dp)
        return str(dp[target])
