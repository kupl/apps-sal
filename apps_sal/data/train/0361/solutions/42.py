class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        h = [0] * m
        self.ans = m * n

        def dfs(h: List[int], cur: int) -> None:
            min_h = min(h)
            if min_h == n:
                self.ans = min(self.ans, cur)
                return
            if cur > self.ans:
                return
            idx = h.index(min_h)
            j = idx
            while j < len(h) and h[j] == min_h:
                j += 1
            fill_width = j - idx
            fill_height = n - min_h
            for fill in range(min(fill_width, fill_height), 0, -1):
                for k in range(idx, idx + fill):
                    h[k] += fill
                dfs(h, cur + 1)
                for k in range(idx, idx + fill):
                    h[k] -= fill
        dfs(h, 0)
        return self.ans
