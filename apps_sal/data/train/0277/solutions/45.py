class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        if len(light) == 1:
            return 1
        mx, mi, s = float('-inf'), float('inf'), 0
        
        res = 0 
        for i, num in enumerate(light):
            s += num
            mx = max(mx, num)
            mi = min(mi, num)
            if mi == 1 and mx == i+1 and s == (i+1)*(i+2)//2:
                res += 1
        
        return res

