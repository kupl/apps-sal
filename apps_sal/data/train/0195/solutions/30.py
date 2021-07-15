class Solution:
    def countTriplets(self, A: List[int]) -> int:
#         N = 1 << 16
#         M = 3
#         dp = [[0]*N for _ in range(M+1)]
#         dp[0][N - 1] = 1
        
#         for i in range(M):
#             for k in range(N):
#                 for a in A:
#                     dp[i+1][k&a] += dp[i][k]
        
#         return dp[M][0]
    
        N = len(A)
        ans = 0
        count = collections.Counter()

        for i in range(N):
            for j in range(N):
                count[A[i]&A[j]] += 1
                
        for k in range(N):
            for v in count:
                if A[k] & v == 0:
                    ans += count[v]
        return ans
