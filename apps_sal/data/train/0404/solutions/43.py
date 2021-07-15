class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        
        n = len(A)
        dp = [[0 for k in range(K)] for i in range(n)]
        for k in range(K):
            dp[0][k] = A[0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] * i / (i+1) + A[i] / (i+1)
        for k in range(1, K):
            for i in range(1, n):
                dp[i][k] = dp[i][k-1]
                for j in range(i):
                    dp[i][k] = max(dp[i][k], dp[j][k-1] + sum(A[j+1:i+1])/(i-j))
        return dp[n-1][K-1]
                
        
        
        
        
        
        
        
        
        
#         memo = [[0 for k in range(K)] for i in range(n)]
        
#         def aux(A, cur, k, memo):
#             if cur == len(A):
#                 return 0
#             if memo[cur][k]:
#                 return memo[cur][k]
#             tmp = sum(A[cur:])/(len(A)-cur)
#             if k == 0:
#                 memo[cur][k] = tmp
#                 return tmp
#             for i in range(cur+1, len(A)+1):
#                 tmp = max(tmp, sum(A[cur:i])/(i-cur) + aux(A, i, k-1, memo))
#             memo[cur][k] = tmp
#             return tmp
                
#         return aux(A, 0, K-1, memo)
        
        
        

