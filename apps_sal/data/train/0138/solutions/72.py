class Solution:

    def getMaxLen(self, nums: List[int], reverse=False) -> int:
        zero_pos = -1
        num_negative = 0
        first_negative = -1
        res = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                num_negative += 1
                if first_negative == -1:
                    first_negative = i
            if nums[i] == 0:
                zero_pos = i
                num_negative = 0
                first_negative = -1
            if nums[i] > 0 or nums[i] < 0:
                if num_negative % 2 == 0:
                    res = max(res, i - zero_pos)
                else:
                    res = max(res, i - first_negative)
        return res
