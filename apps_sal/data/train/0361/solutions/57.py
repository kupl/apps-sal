class Solution:

    def tilingRectangle(self, m: int, n: int) -> int:
        ans = m * n

        def helper(h=[0] * n, res=0):
            nonlocal ans
            if all((x == m for x in h)):
                ans = min(ans, res)
                return
            if res >= ans:
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
        helper()
        return ans
