class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        dp_po, dp_ne = [0] * (len(nums) + 1), [0] * (len(nums) + 1)

        for i, value in enumerate(nums):
            if value == 0:
                dp_po[i + 1] = 0
                dp_ne[i + 1] = 0
            elif value > 0:
                dp_po[i + 1] = dp_po[i] + 1
                if dp_ne[i] > 0:
                    dp_ne[i + 1] = dp_ne[i] + 1
            else:
                dp_ne[i + 1] = dp_po[i] + 1
                if dp_ne[i] > 0:
                    dp_po[i + 1] = dp_ne[i] + 1
            if dp_po[i + 1] > res:
                res = dp_po[i + 1]

        return res
