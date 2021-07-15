class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        if not ranges: return 0
        N = len(ranges)
        # For all location of taps, store the largest right reach point
        max_right_end = list(range(N))
        for i, a in enumerate(ranges):
            max_right_end[max(i - a, 0)] = min(i + a, N-1)
        print(max_right_end)
        res, l, r = 0, 0, max_right_end[0]
        while True:
            res += 1
            # if r can reach to the end of the whole garden, return res
            if r>=N-1:return res
            new_r = max(max_right_end[l:r+1])
            # if next r is same as current r, it means we can not move forward, return -1
            if new_r == r:return -1
            l, r = r, new_r

