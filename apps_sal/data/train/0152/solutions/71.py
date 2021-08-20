class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        lo = 1
        hi = position[-1] - position[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.check(position, mid, m):
                lo = mid
            else:
                hi = mid - 1
        return hi

    def check(self, pos, x, m):
        remain_ball = m - 1
        n = len(pos)
        prev = 0
        for i in range(1, n):
            if pos[i] - pos[prev] >= x:
                remain_ball -= 1
                prev = i
                if remain_ball == 0:
                    return True
            else:
                continue
        return False
