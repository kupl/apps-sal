class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        (min_range, max_range, open_taps) = (0, 0, 0)
        while max_range < n:
            for (i, r) in enumerate(ranges):
                if i - r <= min_range and i + r >= max_range:
                    max_range = i + r
            if min_range == max_range:
                return -1
            open_taps += 1
            min_range = max_range
        return open_taps
