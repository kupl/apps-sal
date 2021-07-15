class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        def cost(a, b):
            alen, blen = len(a), len(b)
            minlen = min(alen, blen)
            for i in range(minlen - 1,0,-1):
                if a[alen - i:] == b[:i]:
                    return blen - i
            return blen
        n = len(A)
        g = [[-1] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if j == i: continue
                g[i][j] = cost(A[i],A[j])

        dp = [[float('inf')] * n for _ in range(1<<n)]
        parent = [[-1] * n for _ in range(1<<n)]
        anslen = float('inf')
        cur = -1
        ans = ''
        for i in range(n):
            dp[1<<i][i] = len(A[i])
        for s in range(1, 1<<n):
            for j in range(n):
                if (s & (1<<j)) == 0: continue
                ps = s & ~(1 << j)
                for i in range(n):
                    if i == j: continue
                    if dp[s][j] > dp[ps][i] + g[i][j]:
                        dp[s][j] = dp[ps][i] + g[i][j]
                        parent[s][j] = i

        for i in range(n):
            if anslen > dp[(1<<n)-1][i]:
                anslen = dp[(1<<n)-1][i]
                cur = i
        s = (1 << n) - 1
        while s > 0:
            ps = s & ~(1 << cur)
            parent_node = parent[s][cur]
            if ps == 0:
                ans = A[cur] + ans
            else:
                curstr = A[cur]
                ans = curstr[len(curstr) - g[parent_node][cur]:] + ans
            s = ps
            cur = parent_node
        return ans
