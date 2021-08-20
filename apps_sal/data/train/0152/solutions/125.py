class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def posb(t):
            k = 0
            s = 0
            for i in range(n - 1):
                k += position[i + 1] - position[i]
                if k >= t:
                    k = 0
                    s += 1
            return s >= m - 1
        hgh = position[-1] - position[0]
        low = 0
        while low < hgh:
            mid = hgh - (hgh - low) // 2
            if posb(mid):
                low = mid
            else:
                hgh = mid - 1
        return low
