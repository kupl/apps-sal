class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def possible(mid):
            temp = m - 1
            prev = position[0]
            for i in range(len(position)):
                if position[i] - prev >= mid:
                    prev = position[i]
                    temp -= 1
            return temp <= 0
        (l, r) = (0, max(position))
        position.sort()
        while l < r:
            mid = (l + r) // 2
            print((l, mid, r))
            if r == l + 1:
                if possible(r):
                    l = r
                else:
                    r = l
                break
            if possible(mid):
                l = mid
            else:
                r = mid - 1
        return l
