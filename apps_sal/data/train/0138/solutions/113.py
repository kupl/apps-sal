class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        (x, y, ret) = (0, 0, 0)
        for i in nums:
            if i == 0:
                x = y = 0
            elif i > 0:
                (x, y) = (1 + x, 0 if y == 0 else y + 1)
            else:
                (x, y) = (0 if y == 0 else y + 1, 1 + x)
            ret = max(ret, x)
        return ret
