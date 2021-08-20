class Solution:
    res = float('inf')

    def tilingRectangle(self, n: int, m: int) -> int:
        s = {}

        def dfs(n, m, h, cnt):
            if cnt > self.res:
                return
            is_full = True
            pos = -1
            minh = float('inf')
            for i in range(1, n + 1):
                if h[i] < m:
                    is_full = False
                if h[i] < minh:
                    pos = i
                    minh = h[i]
            if is_full:
                self.res = min(cnt, self.res)
                return
            key = 0
            base = m + 1
            for i in range(1, n + 1):
                key += h[i] * base
                base *= m + 1
            if key in s and s[key] <= cnt:
                return
            s[key] = cnt
            end = pos
            while end < n and h[end + 1] == h[pos] and (end + 1 - pos + 1 + minh <= m):
                end += 1
            for j in range(end, pos - 1, -1):
                curh = j - pos + 1
                nex = h[:]
                for k in range(pos, j + 1):
                    nex[k] += curh
                dfs(n, m, nex, cnt + 1)
        if n == m:
            return 1
        if n > m:
            (n, m) = (m, n)
        dfs(n, m, [0] * (n + 1), 0)
        return self.res
