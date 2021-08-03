class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        new_ranges = []
        for i in range(len(ranges)):
            new_ranges.append([max(0, i - ranges[i]), min(n, i + ranges[i])])

        new_ranges = sorted(new_ranges, key=lambda x: x[0])

        tap_counter = 0
        ranges_counter = 0
        i = 0
        while i < n:
            # Find all ranges with a start value lower than the current_counter
            max_right = -1
            while ranges_counter < len(new_ranges) and new_ranges[ranges_counter][0] <= i:
                max_right = max(max_right, new_ranges[ranges_counter][1])
                ranges_counter += 1

            if max_right == -1:
                return -1

            tap_counter += 1

            i = max_right

        return tap_counter
