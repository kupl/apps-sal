class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n > m:
            n, m = m, n

        res = [m * n]
        dp = {}

        def dfs(cnt, hs):
            if cnt > res[0]:
                return
            key = tuple(hs)
            if key in dp and dp[key] < cnt:
                return
            dp[key] = cnt
            if all(h == n for h in hs):
                res[0] = min(res[0], cnt)
                return

            min_h = min(hs)
            min_i = hs.index(min_h)
            r = m
            for i in range(min_i, m):
                if hs[i] > min_h:
                    r = i
                    break
            for side in range(min(r - min_i, n - min_h), 0, -1):
                dfs(cnt + 1, hs[:min_i] + [side + min_h] * side + hs[min_i + side:])
        dfs(0, [0] * m)
        return res[0]
