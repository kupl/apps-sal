class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        (res, mx) = (0, 0)
        for (i, v) in enumerate(light, 1):
            mx = max(v, mx)
            res += i == mx
        return res
