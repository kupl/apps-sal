class Solution:

    def tilingRectangle(self, m: int, n: int) -> int:
        ans = m * n

        def helper(h=[0] * n, res=0):
            nonlocal ans
            if h == [m] * n:
                ans = min(ans, res)
                return
            if res >= ans:
                return
            ind = h.index(min(h))
            r = ind + 1
            while r < min(n, ind + m - h[ind] + 1) and h[r] == h[ind]:
                r += 1
            for i in range(r - ind, 0, -1):
                new_h = h[:]
                for j in range(ind, ind + i):
                    new_h[j] += i
                helper(new_h, res + 1)
        helper()
        return ans
