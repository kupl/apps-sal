class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        sorted_ranges = [(max(0, i - v), min(n, i + v)) for (i, v) in enumerate(ranges)]
        dicts = {}
        for i in sorted_ranges:
            dicts[i[0]] = max(i[1], dicts.get(i[0], -10000000000.0))
        reduced_ranges = sorted([(k, v) for (k, v) in dicts.items()])
        prev_max = max_e = reduced_ranges[0][1]
        min_start = reduced_ranges[0][0]
        taps = 1
        i = 0
        (s, e) = reduced_ranges[i]
        print(reduced_ranges)
        while max_e < n:
            taps += 1
            while True:
                (s, e) = reduced_ranges[i + 1]
                if s > prev_max:
                    break
                max_e = max(e, max_e)
                i += 1
                if max_e >= n:
                    return taps
            if max_e == prev_max:
                return -1
            prev_max = max_e
            max_e = max_e
        return taps
