class Solution:
    def distinctSubseqII(self, s: str) -> int:        
        dp = Counter()
        for c in s: dp[c] = sum(dp.values()) + 1
        return sum(dp.values()) % (10**9+7)
