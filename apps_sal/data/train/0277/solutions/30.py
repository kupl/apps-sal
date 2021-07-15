class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        c=0
        mx=0
        for i in range(len(light)):
            a = light[i]
            mx=max(mx,a)
            if mx==i+1:
                c+=1
        return c
