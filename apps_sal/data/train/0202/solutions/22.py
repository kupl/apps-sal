class Solution:

    def longestMountain(self, A: List[int]) -> int:
        if not A:
            return 0
        rising = None
        curr = 0
        best = 0
        prev = None
        for (i, x) in enumerate(A):
            print((i, ':', x, 'curr', curr))
            if prev is None:
                prev = x
                curr = best = 1
                continue
            if rising is None and x < prev:
                prev = x
                continue
            if rising is None and x > prev:
                rising = True
                prev = x
                curr = 2
                continue
            if rising and x > prev:
                curr += 1
            elif not rising and x < prev:
                curr += 1
            elif x == prev:
                rising = None
                best = max(best, curr)
            elif rising and x < prev:
                rising = False
                curr += 1
            elif not rising and x > prev:
                best = max(best, curr)
                rising = True
                curr = 2
            prev = x
        if rising is not None and (not rising):
            best = max(best, curr)
        return 0 if best < 3 else best
