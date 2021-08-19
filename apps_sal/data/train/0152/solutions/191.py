from typing import List, Dict


class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        a = position
        a.sort()
        M = m

        def isok(m):
            c = 0
            prev = -(1 << 30)
            for x in a:
                if x - prev >= m:
                    c += 1
                    prev = x
            return c >= M
        l = 0
        r = 10 ** 9
        while l < r:
            m = (l + r + 1) // 2
            if isok(m):
                l = m
            else:
                r = m - 1
        return l


def _case(*a):
    assert Solution().maxDistance(*a[:-1]) == a[-1]
    pass


def test():
    _case([1, 100], 2, 99)
    _case([1, 2, 3, 4, 7], 3, 3)
    _case([5, 4, 3, 2, 1, 1000000000], 2, 999999999)
    pass
