class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        lowest_missing = 0
        taps = 0
        while lowest_missing < n:
            highest = None
            for (idx, tap) in enumerate(ranges):
                if idx - tap > lowest_missing or idx + tap < lowest_missing + 1:
                    continue
                    
                if highest is None or highest < idx + tap:
                    highest = idx + tap
                
            if highest is None:
                return -1
            
            lowest_missing = highest
            taps += 1
            
        return taps

