class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        dp_pos = [0] * (len(nums) + 1)
        dp_neg = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            if nums[i] > 0:
                dp_pos[i + 1] = dp_pos[i] + 1
                if dp_neg[i] == 0:
                    dp_neg[i + 1] = 0
                else:
                    dp_neg[i + 1] = dp_neg[i] + 1
            elif nums[i] < 0:
                dp_neg[i + 1] = dp_pos[i] + 1
                if dp_neg[i] == 0:
                    dp_pos[i + 1] = 0
                else:
                    dp_pos[i + 1] = dp_neg[i] + 1
        return max(dp_pos)
