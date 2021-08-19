class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        full_ranges = []
        for i in range(n + 1):
            r = (i - ranges[i], i + ranges[i])
            full_ranges.append(r)
        full_ranges.sort()
        range_idx = 0
        covered_max = 0
        num_taps = 0
        while covered_max < n and range_idx < len(full_ranges):
            if full_ranges[range_idx][0] > covered_max:
                return -1
            furthest = -1
            while range_idx < len(full_ranges) and full_ranges[range_idx][0] <= covered_max:
                furthest = max(furthest, full_ranges[range_idx][1])
                range_idx += 1
            assert furthest != -1
            num_taps += 1
            covered_max = furthest
        if covered_max < n:
            return -1
        else:
            return num_taps
