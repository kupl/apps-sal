class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        if m == n:
            return 1
        if n > m:
            (m, n) = (n, m)
        h_i = [0] * n
        visited = {}
        res = [m * n]

        def dfs(height, cnt):
            if cnt > res[0]:
                return
            status = tuple(height)
            if status in visited and visited[status] <= cnt:
                return
            visited[status] = cnt
            complete = True
            start_j = -1
            lowest_h = m + 1
            for j in range(n):
                if height[j] < m:
                    complete = False
                if height[j] < lowest_h:
                    start_j = j
                    lowest_h = height[j]
            if complete:
                res[0] = min(res[0], cnt)
                return
            j = start_j
            while j < n and height[j] == lowest_h:
                j += 1
            max_l = min(j - start_j, m - lowest_h)
            for l in range(max_l, 0, -1):
                next_h = list(height)
                for k in range(l):
                    next_h[start_j + k] += l
                dfs(next_h, cnt + 1)
        dfs(h_i, 0)
        return res[0]
