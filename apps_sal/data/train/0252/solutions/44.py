class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        windows = []

        for i, range in enumerate(ranges):
            windows.append((max(0, i-range), i+range))
        
        windows.sort()
        
        i = 0
        max_water = 0
        num_taps = 0
        
        while i < len(windows):
            if max_water >= n:
                return num_taps
            
            num_taps += 1
            prev_water = max_water
            j = i
            
            while j < len(windows) and windows[j][0] <= prev_water:
                if windows[j][1] > max_water:
                    max_water = windows[j][1]
                    
                j += 1
            
            if max_water == prev_water:
                break
            
            i = j
        
        return -1 if max_water < n else num_taps
