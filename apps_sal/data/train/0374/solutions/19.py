class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        def dist(a, b):
            d = len(b)
            for i in range(min(len(a), len(b)), 0, -1):
                if a[-i:] == b[:i]: return len(b) - i                    
            return d
        
        def build_graph():
            g = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    g[i][j] = dist(A[i], A[j])
            return g
        
        def get_dp():
            dp = [[sys.maxsize]*n for _ in range(1<<n)]
            parent = [[-1]*n for _ in range(1<<n)]
            for i in range(n): dp[1<<i][i] = len(A[i])
            for s in range(1, 1<<n):
                for j in range(n):
                    if not s & (1<<j): continue
                    ps = s & ~(1<<j)
                    for i in range(n):
                        if dp[ps][i] + g[i][j] < dp[s][j]:
                            dp[s][j] = dp[ps][i] + g[i][j]
                            parent[s][j] = i
            return dp, parent
        
        def recover_path():
            j = dp[-1].index(min(dp[-1]))
            s = (1<<n) - 1
            ans = ''
            while s:
                i = parent[s][j]
                if i < 0: ans = A[j] + ans
                else: ans = A[j][(len(A[j])-g[i][j]):] + ans
                s &= ~(1<<j)
                j = i
            return ans
        
        n = len(A)
        g = build_graph()
        dp, parent = get_dp()
        ans = recover_path()
        return ans

