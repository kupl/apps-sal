class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 0
        right = position[-1] - position[0]
        best = 0
        while left <= right:
            target = left + (right - left) // 2
            if self.solve(position, m, target):
                left = target + 1
                best = max(best, target)
            else:
                right = target - 1
        return best

    def solve(self, position, m, target):
        p = position[0]
        m -= 1
        for p2 in position[1:]:
            if p2 - p >= target:
                m -= 1
                p = p2
            if m == 0:
                return True
        return False
