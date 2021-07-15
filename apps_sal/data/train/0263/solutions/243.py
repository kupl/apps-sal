class Solution:
    def knightDialer(self, n: int) -> int:
        mod = int(1e9)+7
        d = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7:[2,6], 8: [1,3], 9:[2, 4], 0: [4,6]}
        ans = {}
        # 1,3; 4,6; 7,9
        @lru_cache(maxsize=None)
        def dfs(i, n):
            nonlocal d
            if n == 0: return 1
            ans = 0
            for val in d[i]:
                ans += dfs(val, n-1)
            return ans    
        for i in range(10):
            if i in [3,6,9]:
                ans[i] = ans[i-2]
            else:    
                ans[i] = dfs(i, n-1)
        #print(ans)                
        return sum(ans.values()) % mod
        # mod = int(1e9)+7
        # d = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7:[2,6], 8: [1,3], 9:[2, 4], 0: [4,6]}
        # cache = collections.defaultdict(int)
        # #@lru_cache(maxsize=None)
        # def dfs(i, n):
        #     if i in [3,6,9] and cache[i-2, n] != 0: return cache[i-2, n]
        #     if i in [1,4,7] and cache[i+2, n] != 0: return cache[i+2, n]
        #     nonlocal d
        #     if not n: return 1
        #     s = sum(dfs(val, n-1) for val in d[i])
        #     cache[i, n] = s
        #     return s
        # 
        # return sum(dfs(i, n-1) for i in range(10)) % mod

