class Solution:

    def numTimesAllBlue(self, light):
        cnt = 0
        (maxV, size) = (0, 0)
        for v in light:
            size += 1
            if v > maxV:
                maxV = v
            if maxV == size:
                cnt += 1
        return cnt
