class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        open_ranges = sorted([(idx-span, idx+span) for idx, span in enumerate(ranges)])
        start, end, count = 0, 0, 0
        i = 0
        while i < len(ranges):
            for j in range(i, len(ranges)):
                l, r = open_ranges[j]
                if l <= start:
                    if r >= end:
                        end = r
                        i = j
            count += 1
            if end >= n:
                return count
            if start == end:
                return -1
            start = end

