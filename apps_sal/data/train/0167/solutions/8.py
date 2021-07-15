class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        
        dp = range(N+1)
        for i in range(2, K+1):
            k = 1
            temp =[0] + [N + 1] * (N)
            for j in range(1, N+1):
                while k < j+1 and temp[j-k] > dp[k-1]:
                    k += 1
                temp[j] = 1 + dp[k-1]
            dp = temp[:]
        return dp[-1]   
