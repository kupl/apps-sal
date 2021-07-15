class Solution:
    def knightDialer(self, n: int) -> int:
        
        d = {1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[3,9,0],
            5:[],
            6:[1,7,0],
            7:[2,6],
            8:[1,3],
            9:[2,4],
            0:[4,6]}
        
        cache = {}
        
        def dfs(l,m):
            nonlocal d
            nonlocal cache
            key = (l,m)
            
            if key in cache:
                return cache[key]
            
            if m == n:
                return 1
            
            ans = 0
            
            for v in d[l]:
                ans += dfs(v,m+1)
                
            cache[key] = ans
            return ans
        
        ret = 0
        for i in range(10):
            ret += dfs(i,1)
                
        return ret%(10**9 +7)
