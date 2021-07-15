from heapq import heappush, heappop 
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
                
        taps_by_start = []  # ranked by start
        for i, r in enumerate(ranges):
            if r != 0:
                tap = (max(0, i-r), i+r) # start, end
                heappush(taps_by_start, tap)
        # print(taps_by_start)

        taps_by_end = [] # the largest end at top 
        current_min = 0
        num_of_pipe= 0
        
        while current_min < n:
            while taps_by_start and taps_by_start[0][0] <= current_min:
                tap = heappop(taps_by_start)
                tap_reverse = (-tap[1], tap[0])
                heappush(taps_by_end, tap_reverse)

            if taps_by_end:
                next_pipe = heappop(taps_by_end)  # -end, start
                current_min = - next_pipe[0]
                num_of_pipe +=1 
            else: 
                return -1 
        
        return num_of_pipe 
         

