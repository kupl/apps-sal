class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        for i, r in enumerate(ranges):
            left = max(0, i-r)
            right = i+r
            ranges[left] = max(ranges[left], right)
            
        l, r, res = 0, 0, 0
            
        while r < n:
            jump = max(ranges[l:r+1])
            if r == jump:
                return -1
            res += 1
            l, r = r, jump
    
        return res

