class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # cover[i] shows the list number of taps needed to cover 0-i
        # inf for impossible
        cover = [math.inf] * n
        
        for i, r in enumerate(ranges):
            start = max(i-r, 0)
            end = min(i+r, n)
            
            pre_min = cover[start-1] if start > 0 else 0
            for j in range(start, end):
                cover[j] = min(cover[j], 1+pre_min)
    
        return cover[-1] if cover[-1] != math.inf else -1
