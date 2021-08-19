class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == 1 and nums[j] == 1:
                if j - i - 1 < k:
                    return False
            if nums[i] == 0 or nums[j] == 1:
                i = j
            j += 1
        return True
