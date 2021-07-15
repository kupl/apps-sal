class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        P = [0]
        for x in A: 
            P.append(P[-1] + x)
        
        def average(i, j):
            return (P[j] - P[i]) / float(j - i)

        N = len(A)
        dp = [average(i, N) for i in range(N)]
        print(dp)
        for k in range(K-1):
            for i in range(N):
                for j in range(i+1, N):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        return dp[0]
        
#         N = len(A)
#         cache = dict()
#         def getMaxScore(i,k):
#             if k <= 0:
#                 return 0
#             if (i,k) in cache:
#                 return cache[(i,k)]
            
#             maxScore = -float(\"inf\")
#             for j in range(i,N):
#                 leftArray = A[i:j+1]
#                 # print(leftArray)
#                 score = float(sum(leftArray))/len(leftArray) + getMaxScore(min(j+1,N),k-1)
#                 maxScore = max(maxScore,score)
                
#             cache[(i,k)] = maxScore
#             return maxScore
        
#         return getMaxScore(0,K)
                

