from heapq import heappush, heappop


class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps_by_start = []
        for (i, r) in enumerate(ranges):
            if r != 0:
                tap = (max(0, i - r), i + r)
                heappush(taps_by_start, tap)
        taps_by_end = []
        current_min = 0
        num_of_pipe = 0
        while current_min < n:
            while taps_by_start and taps_by_start[0][0] <= current_min:
                tap = heappop(taps_by_start)
                tap_reverse = (-tap[1], tap[0])
                heappush(taps_by_end, tap_reverse)
            if taps_by_end:
                next_pipe = heappop(taps_by_end)
                current_min = -next_pipe[0]
                num_of_pipe += 1
            else:
                return -1
        return num_of_pipe
