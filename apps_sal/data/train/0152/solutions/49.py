def solve(positions, m, target):
    p = positions[0]
    m -= 1
    for p2 in positions[1:]:
        if p2 - p >= target:
            m -= 1
            p = p2
        if m == 0:
            return True
    return False


class Solution:
    def maxDistance(self, positions: List[int], m: int) -> int:
        positions.sort()
        l, r = 0, positions[-1] - positions[0]
        best = 0
        while l <= r:
            target = (l + r) // 2
            if solve(positions, m, target):
                l = target + 1
                best = max(best, target)
            else:
                r = target - 1
        return best
