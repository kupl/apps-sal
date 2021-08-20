class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        start = 0
        end = 0
        count_negative = 0
        max_len = 0
        while end < len(nums):
            if nums[end] == 0:
                if count_negative % 2 != 0:
                    while nums[start] > 0:
                        start += 1
                    max_len = max(max_len, end - start - 1)
                start = end = end + 1
                count_negative = 0
            else:
                if nums[end] < 0:
                    count_negative += 1
                if count_negative % 2 == 0:
                    max_len = max(max_len, end - start + 1)
                if end == len(nums) - 1 and count_negative % 2 == 1:
                    while nums[start] > 0:
                        start += 1
                    max_len = max(max_len, end - start)
                end += 1
        return max_len
