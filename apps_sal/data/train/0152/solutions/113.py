class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        hi = position[-1] - position[0] + 1
        lo = 0

        def x(target):
            currMin = position[0]
            count = 1
            for pos in position:
                if pos - currMin >= target:
                    currMin = pos
                    count += 1
                if count >= m:
                    return False
            return True
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if x(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo - 1
