class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        right = 0
        ans = 0
        for i in range(len(light)):
            if (light[i] > right):
                right = light[i]
            
            if (i + 1 == right):
                ans += 1
                
        return ans
