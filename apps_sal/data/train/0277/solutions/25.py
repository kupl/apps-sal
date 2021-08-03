class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        bSum = 0
        pSum = 0
        rr = 0
        for i in range(len(light)):
            bSum += light[i]
            pSum += i + 1
            if bSum == pSum:
                rr += 1
        return rr
