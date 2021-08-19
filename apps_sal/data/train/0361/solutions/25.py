class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        if n < m:
            return self.tilingRectangle(m, n)
        h = [0] * m
        self.ans = 100000
        self.dfs(n, m, h, 0)
        return self.ans

    def dfs(self, m, n, h, cur):
        if cur >= self.ans:
            return
        min_h = min(h)
        if min_h == m:
            self.ans = min(self.ans, cur)
            return
        for j in range(n):
            if h[j] == min_h:
                break
        start = j
        while j + 1 < n and h[j] == h[j + 1] and (j + 1 - start + 1 + h[j] <= m):
            j += 1
        side = j - start + 1
        for k in reversed(range(1, side + 1)):
            temp = list(h)
            for j in range(start, start + k):
                temp[j] += k
            self.dfs(m, n, temp, cur + 1)
