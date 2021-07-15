class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        maxv = max(rollMax)
        dp = [[[0] * (maxv + 1) for _ in range(6)] for _ in range(n + 1)]
        
        for j in range(6):
            dp[1][j][1] = 1
        prev_total = 6
            
        for n in range(2, n + 1):
            new_total = 0
            for roll_num in range(6):
                one = prev_total - sum(dp[n - 1][roll_num])
                dp[n][roll_num][1] = one % 1000000007
                for k in range(2, rollMax[roll_num] + 1):
                    dp[n][roll_num][k] = dp[n - 1][roll_num][k - 1]
                new_total += sum(dp[n][roll_num])
            prev_total = new_total
        return sum(sum(dp[-1][number]) for number in range(6)) % 1000000007
