class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        h2p = defaultdict(list)
        n = len(hats)
        mod = 10**9+7
        
        for p, hat_list in enumerate(hats):
            for h in hat_list:
                h2p[h].append(p)
        
        '''
        def dp(h, mask):
            if (h, mask) in memo:
                return memo[(h,mask)]
            
            if mask == (1 << n) - 1:
                return 1
        
            if h > 40:
                return 0
            
            ans = dp(h+1, mask)
            
            if h in h2p:
                peoples = h2p[h]
                
                for p in peoples:
                    if mask & (1 << p) == 0:
                        mask |= (1 << p)
                        ans += dp(h+1, mask)
                        mask ^= (1 << p)
            
            memo[(h,mask)] = ans
            
            return ans
        
        memo = {}
        
        return dp(0, 0) % mod
        '''
        m = 1 << n
        
        dp = [[0] * m for _ in range(41)]
        
        dp[0][0] = 1
        
        for h in range(1, 41):
            for mask in range(m):
                dp[h][mask] = dp[h-1][mask]
                
                for p in h2p[h]:
                    if mask & (1 << p) != 0:
                        dp[h][mask] += dp[h-1][mask ^ (1 << p)]
    
        return dp[40][m-1] % mod
                    

