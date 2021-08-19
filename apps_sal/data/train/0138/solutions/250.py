class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        f_pos = 0
        f_neg = 0
        max_pos = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                (f_pos, f_neg) = (0, 0)
            elif nums[i] > 0:
                f_pos += 1
                if f_neg > 0:
                    f_neg += 1
            else:
                tmp = f_pos
                if f_neg > 0:
                    f_pos = f_neg + 1
                else:
                    f_pos = 0
                f_neg = tmp + 1
            print((i, f_pos, f_neg))
            max_pos = max(max_pos, f_pos)
        return max_pos
