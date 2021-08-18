class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m:
            return 1
        if m > n:
            m, n = n, m

        @lru_cache(None)
        def helper(skyline):
            if all(h == n for h in skyline):
                return 0

            ans = float('inf')
            minh = min(skyline)
            l = skyline.index(minh)
            r = l
            while r < len(skyline) and skyline[r] == skyline[l] and minh + r - l + 1 <= n:
                r += 1
            r -= 1
            for rr in range(r, l - 1, -1):
                if skyline[rr] != minh:
                    break
                if rr - l + 1 > n - minh:
                    break
                newsl = list(skyline)
                for i in range(l, rr + 1):
                    newsl[i] += rr - l + 1
                ans = min(ans, helper(tuple(newsl)))
            return ans + 1

        ans = helper(tuple([0] * m))
        return ans
