class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        
        MOD = int(1e9 + 7)
        N = len(A)
        
        A.sort()
        dp = [1] * N
        idx = {ele: i for i, ele in enumerate(A)}
        
        for c, rootVal in enumerate(A):
            for j in range(c):
                left = A[j]
                if rootVal % left == 0:
                    right = rootVal / left 
                    if right in idx:
                        dp[c] += dp[j] * dp[idx[right]] % MOD
                        
        return sum(dp) % MOD

