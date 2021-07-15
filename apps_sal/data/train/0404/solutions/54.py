class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        dp=[[0 for j in range(K)] for i in A]
        for j in range(len(A)):
            for i in range(K): 
                if i==0:
                    dp[j][i]=sum(A[:j+1])/len(A[:j+1])
                else:
                    if len(A[:j+1])<i+1:
                        break
                    for k in range(j):
                        dp[j][i]=max(dp[k][i-1]+sum(A[k+1:j+1])/len(A[k+1:j+1]), dp[j][i])
        return dp[-1][-1]

