from math import floor


class Solution:
    def is_min_dis_possible(self, positions, m, min_dis):
        prev = 0
        cur = 0

        while m > 0:
            m -= 1

            while cur < len(positions) and positions[cur] - positions[prev] < min_dis:
                cur += 1

            if cur >= len(positions):
                break

            prev = cur

        return True if m == 0 else False

    def maxDistance(self, position, m):
        position_sorted = sorted(position)
        high = position_sorted[-1]
        low = 0

        while low <= high:
            mid = floor((high + low) / 2)
            if mid == low:
                break

            is_min_dis_possible = self.is_min_dis_possible(position_sorted, m, mid)
            if is_min_dis_possible:
                low = mid
            else:
                high = mid

        return low
