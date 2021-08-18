class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        l = -1
        neg_num = 0
        result = 0
        for i in range(n):
            if (nums[i] == 0):
                while (neg_num % 2):
                    if (nums[l + 1] < 0):
                        neg_num -= 1
                    l += 1
                result = max(result, i - l - 1)
                l = i
                count = 0
            elif (nums[i] < 0):
                neg_num += 1
            if (neg_num % 2 == 0):
                result = max(result, i - l)
        while (neg_num % 2) and (l < n - 1):
            if (nums[l + 1] < 0):
                neg_num -= 1
            l += 1
        result = max(result, n - 1 - l)
        return result
