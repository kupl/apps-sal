class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
#         from collections import defaultdict
        
#         if n==0:
#             return -1
        
#         plots = defaultdict(list)
#         for i in range(n):
#             l, r = i - ranges[i], i + ranges[i]
#             for j in [k for k in range(n) if k>=l and k<=r]:
#                 plots[j].append(i)
        
#         print(plots)
#         if len(plots.keys()) == n:
#             for i in plots.items():
#                 print(i)
#         else:
#             return -1

        def parse_ranges(ranges):
            intervals = []
            
            for idx, distance in enumerate(ranges):
                left = max(0, idx-distance)
                right = min(n, idx+distance)
                intervals.append([left, right])
            
            return intervals
        
        watered = []
        intervals = parse_ranges(ranges)
        intervals.sort(key=lambda time: (time[0], -time[1]))
        for start, end in intervals:
            if watered and watered[-1][1] >= end: 
                continue
            if watered and start - watered[-1][1] > 0: 
                return -1
            
            if len(watered) >= 2 and start <= watered[-2][1]:
                # print(watered, (start,end))
                watered[-1] = [start, end]
            else:
                watered.append([start, end])
        
        return len(watered) if watered[-1][-1] >= n else -1
