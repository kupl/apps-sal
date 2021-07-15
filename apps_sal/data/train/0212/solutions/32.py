class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:   
        A.sort()
        numToIdx = {x : i for i, x in enumerate(A)}
        
        dp = [1 for _ in range(len(A))]
        
        MOD = 10**9 + 7
        totalSum = 0
        
        for i, x in enumerate(A):
            for j in range(i):
                y = A[j]
                if x % y == 0 and x // y in numToIdx:
                    dp[i] += dp[j] * dp[numToIdx[x // y]]
            
            totalSum = (totalSum + dp[i]) % MOD
        
        return totalSum
