class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        last_zero = last_negative = -1
        running_count = 0
        negative_count = 0
        for (i, v) in enumerate(nums):
            if v == 0:
                last_zero = last_negative = i
                running_count = zero_count = negative_count = 0
            elif v < 0:
                negative_count += 1
                if negative_count == 1:
                    last_negative = i
                if negative_count % 2 == 0:
                    ans = max(ans, i - last_zero)
                else:
                    ans = max(ans, i - last_negative)
            elif negative_count % 2 == 0:
                ans = max(ans, i - last_zero)
            else:
                ans = max(ans, i - last_negative)
        return ans
