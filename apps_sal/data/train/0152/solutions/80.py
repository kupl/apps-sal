class Solution:
    def fit_balls(self, positions, n, min_dist):
        if n == 0:
            return True

        if len(positions) < 1:
            return False

        last_position = positions[0]
        placement_count = 1

        for p in positions:
            if p - last_position >= min_dist:
                last_position = p
                placement_count += 1

        return n <= placement_count

    def maxDistance(self, position: List[int], m: int) -> int:
        pos = sorted(position)

        lo = 0
        hi = pos[-1] - pos[0]

        while lo < hi:
            mid = hi - (hi - lo) // 2
            can_fit = self.fit_balls(pos, m, mid)

            if not can_fit:
                hi = mid - 1
            else:
                lo = mid

        return lo
