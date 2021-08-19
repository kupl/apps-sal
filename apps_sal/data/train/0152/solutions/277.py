class Solution:
    def maxDistance(self, p: List[int], m: int) -> int:
        n = len(p)
        p.sort()

        def check(x):
            st = p[0]
            cnt = 1
            for i in range(1, n):
                if abs(p[i] - st) >= x:
                    st = p[i]
                    cnt += 1
            return cnt >= m
        lo = 1
        hi = max(p) + 4
        print(check(999999999))
        while lo <= hi:
            mi = (lo + hi) // 2
            if check(mi):
                ans = mi
                lo = mi + 1
            else:
                hi = mi - 1
            # print(mi,check(mi))
        return ans
