class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def bs(mid, m):
            pre = position[0]
            m -= 1
            for x in position:
                if x - pre >= mid:
                    pre = x
                    m -= 1
                    if m == 0:
                        return True
            if m == 0:
                return True
            else:
                return False
        l = 1
        r = 10 ** 9
        position.sort()
        while l < r:
            mid = l + (r - l) // 2
            if bs(mid, m):
                l = mid + 1
            else:
                r = mid
        return l - 1
