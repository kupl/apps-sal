class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        r = 0
        c = 0
        for i in range(len(light)):
            r = max(r, light[i])
            if(r == i + 1):
                c = c + 1
        return c
