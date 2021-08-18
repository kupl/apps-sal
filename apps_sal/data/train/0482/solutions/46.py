class Solution:
    def mctFromLeafValues(self, a: List[int]) -> int:
        n = len(a)
        cache = [[[-1, -1]] * n for i in range(n)]

        def dp(i, j):
            if(i == j):
                return [0, a[i]]
            if(cache[i][j] != [-1, -1]):
                return cache[i][j]
            ans = float('inf')
            mx = 0
            for k in range(i, j):
                l = dp(i, k)
                r = dp(k + 1, j)
                mx = max(mx, l[1])
                mx = max(mx, r[1])
                ans = min(ans, l[0] + r[0] + l[1] * r[1])
            cache[i][j] = [ans, mx]
            return [ans, mx]
        return dp(0, n - 1)[0]
