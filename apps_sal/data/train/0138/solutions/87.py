class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        left = right = negCount = negIndex = res = 0
        while right <= len(nums):
            if right < len(nums) and nums[right] != 0:
                if nums[right] < 0:
                    negCount += 1
                    negIndex = right
                right += 1
            else:
                if negCount % 2 == 1:
                    res = max(res, negIndex - left)
                    while nums[left] > 0:
                        left += 1
                    res = max(res, right - left - 1)
                else:
                    res = max(res, right - left)
                right += 1
                left = right
                negCount = 0
        return res
