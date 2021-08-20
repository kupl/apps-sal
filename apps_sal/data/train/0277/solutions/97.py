class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        count = 0
        max_idx = 0
        res = 0
        for p in light:
            max_idx = max(max_idx, p - 1)
            count += 1
            if count == max_idx + 1:
                res += 1
        return res
