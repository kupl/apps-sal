class Solution:

    def minSubArrayLen(self, s, nums):
        """two pointers. 在一个循环完成后,[i-1,j]必然是[0,j]中最短的
        符合要求的区间. 故i-1前作为起点,j前作为终点的区间可不考虑,
        即截掉i-1之前的区间."""
        i = 0
        j = 0
        tempSum = 0
        length = len(nums)
        minLength = 2147483647
        while i < length and j < length:
            while j < length:
                tempSum += nums[j]
                if tempSum >= s:
                    break
                j += 1
            if j < length:
                minLength = min(j - i + 1, minLength)
                while i <= j:
                    if tempSum < s:
                        break
                    tempSum -= nums[i]
                    i += 1
                minLength = min(j - i + 2, minLength)
                j += 1
        if minLength == 2147483647:
            return 0
        else:
            return minLength
