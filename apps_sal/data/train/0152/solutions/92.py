class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def isPossible(lst, m, force):
            pos = lst[0]
            for i in range(1, len(lst)):
                if lst[i] - pos >= force:
                    m -= 1
                    pos = lst[i]
            return m < 2

        l = 0
        r = 1000000000
        position.sort()

        while l < r:
            mid = ((l + r) >> 1) + 1
            if isPossible(position, m, mid):
                l = mid
            else:
                r = mid - 1
        return l
