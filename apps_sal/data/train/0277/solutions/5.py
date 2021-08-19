import bisect


class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        sl = []
        count = 0
        for k in range(len(light)):
            bisect.insort_right(sl, light[k])
            if len(sl) == sl[-1]:
                count = count + 1
        return count
