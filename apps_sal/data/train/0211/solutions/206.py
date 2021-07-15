class Solution:
    def maxUniqueSplit(self, s: str) -> int:        
        def dfs(i, vis):
            nonlocal ans            
            if len(vis) + n-i < ans: return
            if i >= n: ans = max(ans, len(vis))                
            l = n-i
            for k in range(1, l+1):
                x = s[i:i+k]
                if x not in vis: 
                    vis.add(x)
                    dfs(i+k, vis)
                    vis.discard(x)
        ans, n, vis = 0, len(s), set()
        dfs(0, vis)
        return ans
