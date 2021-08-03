class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def count(d):
            c = position[0]
            res = 1
            for n in position[1:]:
                if n - c >= d:
                    res += 1
                    c = n
            return res

        l = 1
        r = (position[-1] - position[0]) // (m - 1)
        while l <= r:
            mid = (l + r) // 2
            if count(mid) < m:
                r = mid - 1
            elif count(mid + 1) < m:
                return mid
            else:
                l = mid + 1
        return l
