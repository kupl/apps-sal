class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:        
        hat2ppl = defaultdict(set)        
        for p, hats_i in enumerate(hats):
            for h in hats_i: hat2ppl[h].add(p)

        M, n = 10**9 + 7, 1 << len(hats)
        dp = [0] * n
        dp[0] = 1
        for h in hat2ppl:
            for j in range(n-1, -1, -1):
                for p in hat2ppl[h]:       
                    if j & (1 << p):                        
                        dp[j] = (dp[j] + dp[j ^ (1 << p)]) % M                        
        return dp[-1]                            
