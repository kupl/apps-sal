class Solution:

    def maxDistance(self, pp: List[int], k: int) -> int:
        n = len(pp)
        pp.sort()
        l = 1
        r = pp[-1] - pp[0] + 1

        def ok(m):
            i = 1
            pre = pp[0]
            for _ in range(k - 1):
                while i < n and pp[i] - pre < m:
                    i += 1
                if n == i:
                    return False
                pre = pp[i]
                i += 1
            return True
        while l + 1 < r:
            m = (l + r) // 2
            if ok(m):
                l = m
            else:
                r = m
        return l
