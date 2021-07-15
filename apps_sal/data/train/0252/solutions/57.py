class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        for i, r in enumerate(ranges):
            left = max(0, i-r)
            right = i+r
            ranges[left] = max(ranges[left], right)
            
        r, res = 0, 0
            
        while r < n:
            tmp = r
            r = max(ranges[0:r+1])
            res += 1
            if tmp == r:
                return -1
    
        return res

