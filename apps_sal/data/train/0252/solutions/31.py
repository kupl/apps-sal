class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        min_range, max_range, open_taps, idx = 0, 0 ,0, 0
        
        while max_range < n:
            for i in range(len(ranges)):
                if i - ranges[i] <= min_range and i + ranges[i] >= max_range:
                    max_range = i + ranges[i]
            
            if min_range == max_range:
                return -1
            open_taps += 1
            min_range = max_range
        
        return open_taps

