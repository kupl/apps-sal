class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        num = 0
        maxPos = 0
        res = []
        for i in range(len(light)):
            maxPos = max(maxPos, light[i])
            num += 1
            if num == maxPos:
                res.append(i)
        return len(res)
