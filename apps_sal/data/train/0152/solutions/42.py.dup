class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        length = len(position)
        position.sort()

        def count(d):
            minmax = 1
            curr = position[0]
            for i in range(1, length):
                if position[i] - curr >= d:
                    minmax += 1
                    curr = position[i]
            return minmax

        lo, hi = 0, position[-1] - position[0]
        while lo < hi:
            mid = hi - (hi - lo) // 2
            if count(mid) >= m:
                lo = mid
            else:
                hi = mid - 1
        return lo
