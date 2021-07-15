
# 823. Binary Trees With Factors

class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        
        MOD = int(1e9 + 7)
        N = len(A)
        
        A.sort()
        dp = [1] * N
        idx = {ele: i for i, ele in enumerate(A)}
        
        for c, rootVal in enumerate(A):
            for l in range(c):
                leftVal = A[l]
                if rootVal % leftVal == 0:
                    rightVal = rootVal / leftVal 
                    if rightVal in idx:
                        dp[c] += dp[l] * dp[idx[rightVal]] % MOD
                        
        return sum(dp) % MOD

