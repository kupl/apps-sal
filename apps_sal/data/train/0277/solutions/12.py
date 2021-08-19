class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        cur_max = 0
        count = 0
        res = 0
        for i in light:
            cur_max = max(cur_max, i)
            count += 1
            if count == cur_max:
                res += 1
        return res
