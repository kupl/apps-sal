class Solution:
    def maxDistance(self, a: List[int], m: int) -> int:
        def check(d):
            x, k = 0, m
            for i in range(len(a)):
                if a[i] >= x:
                    x, k = a[i] + d, k - 1
                    if k == 0:
                        break
            return k == 0

        a.sort()
        l, r = 1, (max(a) - min(a)) // (m - 1)
        while l + 1 < r:
            d = (l + r) // 2
            if check(d):
                l = d
            else:
                r = d - 1
        return r if check(r) else l
