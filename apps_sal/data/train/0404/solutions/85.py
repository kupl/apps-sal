class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        #larger sum in subarray group 往dp想，一般都是第一类区间dp
        #这类区间的套路就是dp[i][k] 前i个分成k个group的最优解
        #转移方程
  #      for (i=1; i<=N; i++)
  #         for (k=1; k<=min(i,K); k++)
  #     // find the best break point j （jd的区间就是i - k, c从高到低）
  #             for (int j=i; j>=k; j--)
  #                 dp[i][k] = max(dp[i][k], dp[j-1][k-1] + sum[j:i] );


        n = len(A)
        A = [0] + A
        dp = [[0]*(K+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
             dp[i][0] = -float('inf')
        
        for i in range(1, n+1):
            for k in range(1, min(i+1, K+1)):
                sum_s = 0
                #这里j要从最大的往回走，才能统计sum
                for j in range(i, k-1, -1):
                    sum_s += A[j]
                    dp[i][k] = max(dp[i][k], dp[j-1][k-1] + sum_s/(i-j + 1))
        
        res = 0 
        for i in range(1, K+1):
            res = max(res, dp[n][i])
        
        return res







  # 
#         n = len(A)
#         dp = [[0]*(K+1) for _ in range(n+1)]
        
#         A = [0] + A
        
#         for i in range(1, n+1):
#             dp[i][0] = -float('inf')
        
#         for i in range(1, n+1):
#             for k in range(1, min(K+1, i+1)):
#                 #
#                 sum_s = 0
#                 for j in range(k, i+1):
#                     sum_s += A[j]
#                     dp[i][k] = max(dp[i][k], dp[j-1][k-1] + sum_s//(i-j+1) )
        
#         res = 0
#         for i in range(1, K+1):
#             res = max(res, dp[n][i])
#         print(dp)
#         return res
     
    
    

