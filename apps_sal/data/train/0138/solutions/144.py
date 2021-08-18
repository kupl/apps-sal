class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        from numpy import sign
        while left < len(nums) - ans:
            right = left
            s = 1
            while right < len(nums):
                s *= sign(nums[right])
                if s > 0:
                    ans = max(ans, right - left + 1)
                elif s == 0:
                    break
                right += 1

            if nums[left] > 0:
                while left < len(nums) and nums[left] > 0:
                    left += 1
            else:
                left += 1

        return ans
