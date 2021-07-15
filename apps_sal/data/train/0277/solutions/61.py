class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        ranges = {}
        r = 0
        for l in light:
            if l + 1 not in ranges and l - 1 not in ranges:
                ranges[l] = (l, l)
            elif l + 1 in ranges and l - 1 not in ranges:
                _, rr = ranges[l + 1]
                ranges[l] = ranges[rr] = (l, rr)
                if rr != l + 1:
                    del ranges[l + 1]
            elif l - 1 in ranges and l + 1 not in ranges:
                ll, _ = ranges[l - 1]
                ranges[ll] = ranges[l] = (ll, l)
                if ll != l - 1:
                    del ranges[l - 1]
            else:
                ll, _ = ranges[l - 1]
                _, rr = ranges[l + 1]
                ranges[ll] = ranges[rr] = (ll, rr)
                if ll != l - 1:
                    del ranges[l - 1]
                if rr != l + 1:
                    del ranges[l + 1]
            # print(ranges)
            if len(ranges) == 1:
                r += (list(ranges.items())[0][0] == 1)
            elif len(ranges) == 2:
                r += (len(set(ranges.values())) == 1 and list(ranges.values())[0][0] == 1)
        return r
