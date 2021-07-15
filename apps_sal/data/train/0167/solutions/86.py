class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
#         # brutal force - time O(kn^2); space O(kn)
#         dp = [[float('inf')] * (N+1) for _ in range(K+1)]
#         for egg_num in range(1, K+1):
#             dp[egg_num][0] = 0
#             dp[egg_num][1] = 1
#         for floor_num in range(1, N+1):
#             dp[1][floor_num] = floor_num
        
#         for egg_num in range(2, K+1):
#             for floor_num in range(2, N+1):
#                 for start_floor in range(1, floor_num+1):
#                     dp[egg_num][floor_num] = min(dp[egg_num][floor_num], 1+max(dp[egg_num-1][start_floor-1], dp[egg_num][floor_num-start_floor]))
#         print(dp)
#         return dp[K][N]
    
        # time - O(nk) for declare and O(klogn) for running; space O(nk)
        dp = [[0] * (K+1) for _ in range(N+1)]
        for m in range(1, N+1):
            for k in range(1, K+1):
                dp[m][k] = dp[m-1][k-1] + dp[m-1][k] + 1
            if dp[m][K] >= N:
                return m
