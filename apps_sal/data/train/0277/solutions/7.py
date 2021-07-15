class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        ans = 0
        maxidx = 0
        
        for i, l in enumerate(light):
            maxidx = max(maxidx, l)
            if i+1 == maxidx:
                ans += 1
        return ans
