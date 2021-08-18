class Solution:
    def tilingRectangle(self, m: int, n: int) -> int:
        self.ans = m * n

        def helper(h, res):

            if all(x == m for x in h):
                self.ans = min(self.ans, res)
                return
            if res >= self.ans:
                return
            temp = min(h)
            ind = h.index(temp)
            r = ind + 1
            while r < min(n, ind + m - temp + 1) and h[r] == temp:
                r += 1
            for i in range(r - ind, 0, -1):
                new_h = h[:]
                for j in range(ind, ind + i):
                    new_h[j] += i
                helper(new_h, res + 1)
        helper([0] * n, 0)
        return self.ans
