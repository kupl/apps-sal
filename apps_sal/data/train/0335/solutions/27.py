class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        rods.sort()
        prefixsum = [0]
        for i in rods:
            prefixsum.append(prefixsum[-1] + i)
        s = prefixsum[-1]
        dp = [-1] * (s + 1) * 2
        dp[s] = 0
        for i in range(n - 1, -1, -1):
            new_dp = [-1] * (s + 1) * 2
            for d in range(-prefixsum[i], prefixsum[i] + 1):
                m = -1
                if prefixsum[-1] - prefixsum[i] < d:
                    new_dp[d + s] = -1
                    break
                if dp[rods[i] + d + s] >= 0:
                    m = max(m, dp[rods[i] + d + s] + rods[i])
                if dp[d - rods[i] + s] >= 0:
                    m = max(m, dp[d - rods[i] + s])
                if dp[d + s] >= 0:
                    m = max(m, dp[d + s])
                new_dp[d + s] = m
            dp = new_dp
        return dp[s]
