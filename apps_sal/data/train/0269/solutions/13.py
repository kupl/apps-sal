class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        zeros = 0
        i = 0
        while i < len(nums):
            if i == 0 and nums[i] == 1:
                i += 1
                continue
            if nums[i] == 1 and zeros < k:
                return False
                break
            elif nums[i] == 0:
                zeros += 1
                i += 1
            elif nums[i] == 1 and zeros >= k:
                zeros = 0
                i += 1
        return True
