class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        positions = sorted(position)
        l, r = 1, positions[len(position) - 1] - positions[0]
        while l < r:
            mid = math.ceil((l + r) / 2)
            if self.balls(positions, mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l

    def balls(self, positions, d):
        curr, ans = -10 ** 10, 0
        for position in positions:
            if position - curr >= d:
                curr = position
                ans += 1
        return ans
