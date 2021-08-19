from math import ceil


class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        (minPos, maxPos) = (position[0], position[len(position) - 1])
        (lo, hi) = (0, maxPos - minPos)
        curAns = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.canFitAllBalls(mid, m, position):
                curAns = max(curAns, mid)
                lo = mid + 1
            else:
                hi = mid - 1
        return curAns

    def canFitAllBalls(self, dist, m, position):
        prev = None
        for pos in position:
            if prev == None or pos - prev >= dist:
                m -= 1
                prev = pos
            if m == 0:
                break
        return m == 0
