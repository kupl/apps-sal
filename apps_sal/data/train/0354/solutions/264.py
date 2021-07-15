MOD = int(1e9 + 7)

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp: List[List[int]] = [[0] * 6 for _ in range(n)]
        sums: List[int] = [0] * n
            
        # Init
        for j in range(6):
            dp[0][j] = 1
            
        sums[0] = sum(dp[0])
        
        # DP
        for i in range(1, n):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        dp[i][j] += 1
                        break

                    dp[i][j] += sums[i - k] - dp[i - k][j]
                    
            sums[i] = sum(dp[i]) % MOD
            
        return sums[-1]
   
# roll_max_2 = 3
# _, _, _, 2 = (_, _, !2, 2) + (_, !2, 2, 2) + (!2, 2, 2, 2)

