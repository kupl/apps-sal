class Solution:
    def distinctSubseqII(self, S: str) -> int:
        K = 1000000000 + 7
        n = len(S)
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        umap = dict()
        
        for i in range(n):
            dp[i+1] = (2 * dp[i]) % K
            if S[i] in umap:
                dp[i+1] -= dp[umap[S[i]]]
            dp[i+1] %= K
            umap[S[i]] = i
        
        result = dp[n] - 1
        if result < 0:
            result += K
        return result
