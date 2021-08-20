class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        if n > m:
            self.tilingRectangle(m, n)
        self.ans = n * m
        h = [0] * n
        self.dfs(h, 0, n, m)
        return self.ans

    def dfs(self, h, cur, n, m):
        if cur >= self.ans:
            return
        min_h = min(h)
        if min_h == m:
            self.ans = cur
            return
        for i in range(n):
            if h[i] == min_h:
                break
        (start, end) = (i, i)
        while end < n and h[start] == h[end] and (end - start + 1 + min_h <= m):
            end += 1
        for i in reversed(list(range(start, end))):
            size = i - start + 1
            for j in range(start, i + 1):
                h[j] += size
            self.dfs(h, cur + 1, n, m)
            for j in range(start, i + 1):
                h[j] -= size
