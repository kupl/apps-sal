class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        max_ind = 0
        res = 0
        for t in range(len(light)):
            max_ind = max(max_ind, light[t])
            if max_ind == t + 1:
                res += 1
        return res
