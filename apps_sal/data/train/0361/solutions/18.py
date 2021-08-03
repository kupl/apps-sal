class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        m, n = min(m, n), max(m, n)
        self.res = n * m
        self.H = n
        self.search(0, [0] * m)
        return self.res

    def search(self, count, heights):
        if count >= self.res:
            return
        min_h = min(heights)
        if min_h == self.H:
            self.res = count
            return
        l = heights.index(min_h)
        width = 1
        while width <= self.H - min_h and l + width - 1 < len(heights) and heights[l + width - 1] == heights[l]:
            width += 1
        width -= 1
        for w in range(width, 0, -1):
            self.search(count + 1, heights[:l] + [min_h + w] * w + heights[l + w:])
