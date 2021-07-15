class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        N = len(A)
        P = [0]
        for a in A:
            P.append(P[-1]+a)

        dp = [0]*(N+1)
        for i in range(K):
            dp2 = [0]*(N+1)
            for j in range(i, N+1):
                if i==0 and j!=0:
                    dp2[j] = P[j]/j
                    continue
                    
                for k in range(i-1, j):
                    dp2[j] = max(dp2[j], dp[k]+(P[j]-P[k])/(j-k))
            
            dp = dp2
        return dp[-1]
