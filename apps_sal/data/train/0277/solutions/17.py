class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        (mn, ma) = (n + 1, 0)
        ans = 0
        for (k, v) in enumerate(light):
            (ma, mn) = (max(ma, v), min(mn, v))
            if mn == 1 and ma - mn == k:
                ans += 1
        return ans

    def numTimesAllBlue(self, light: List[int]) -> int:
        (result, right) = (0, 0)
        for (i, num) in enumerate(light, 1):
            right = max(right, num)
            result += right == i
        return result
