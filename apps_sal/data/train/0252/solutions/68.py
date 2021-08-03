import bisect


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        uc = 0
        taps = []
        taps_r = []
        for idx, r in enumerate(ranges):
            if r > 0:
                tap = (idx - r if idx - r > 0 else 0, idx + r)
                tapr = (idx + r, idx - r if idx - r > 0 else 0)
                taps_r.append(tapr)
                taps.append(tap)
        if not taps:
            return -1
        taps.sort()
        curr_idx = bisect.bisect_left(taps, (1, 0)) - 1
        curr_idx = curr_idx if curr_idx > 0 else 0
        if taps[curr_idx][0] > 0:
            return -1
        e_range = taps[curr_idx][1]
        res = 1
        if e_range >= n:
            return 1
        lo = curr_idx
        hi = len(taps)
        while e_range < n:
            hi = bisect.bisect_left(taps, (e_range + 1, 0), lo, hi)
            print(hi)
            max_e = 0
            for i in range(lo, hi):
                if taps[i][1] > max_e:
                    curr_idx = i
                    max_e = taps[i][1]
            if max_e <= e_range:
                return -1
            e_range = max_e
            lo = curr_idx
            hi = len(taps)
            res += 1
        return res
