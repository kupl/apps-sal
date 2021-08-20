class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        var = 0
        count = 0
        max1 = 0
        pos = 0
        flag = 0
        for i in nums:
            if i == 1:
                flag = 1
                if var == 1:
                    pos = pos + 1
                count = count + 1
                max1 = max(count, max1)
            elif i == 0 and var == 1:
                count = pos
                pos = 0
            elif flag == 1:
                if var == 0:
                    var = var + 1
                else:
                    count = pos
        if max1 == len(nums):
            return max1 - 1
        return max1
