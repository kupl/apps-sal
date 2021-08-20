class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        dp = {}
        if n < m:
            (m, n) = (n, m)
        if m == n:
            return 1
        res = [m * n + 1]

        def dfs(ys, cnt):
            key = tuple(ys)
            if key not in dp or cnt < dp[key]:
                dp[key] = cnt
            if dp[key] < cnt or cnt > res[0]:
                return
            if all((i == m for i in ys)):
                res[0] = min(res[0], cnt)
                return
            if any((i > m for i in ys)):
                return
            ymin = min(ys)
            idx = ys.index(ymin)
            ymax = 0
            for i in range(idx, n):
                if ys[i] > ymin:
                    break
                else:
                    ymax += 1
            ymax = min(ymax, m)
            for i in range(ymax, 0, -1):
                dfs(ys[:idx] + [ys[idx] + i] * i + ys[idx + i:], cnt + 1)
        dfs([0] * n, 0)
        return res[0]
