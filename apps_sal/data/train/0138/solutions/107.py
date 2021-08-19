class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        rst = 0
        max_pos = max_neg = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                max_pos = max_neg = 0
                continue
            if i == 0:
                if nums[i] > 0:
                    max_pos = 1
                else:
                    max_neg = 1
            elif nums[i] > 0:
                if max_neg:
                    max_neg += 1
                max_pos += 1
            else:
                tmp = max_neg
                max_neg = max_pos + 1
                if tmp:
                    max_pos = tmp + 1
                else:
                    max_pos = 0
            rst = max(rst, max_pos)
        return rst
