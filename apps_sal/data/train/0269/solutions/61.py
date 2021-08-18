class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return True
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                break
            i += 1
        counter = 0
        i += 1
        while i < len(nums):
            j = i - 1
            print(nums[j], nums[i])
            if nums[j] == 0 and nums[i] == 1:
                if counter < k:
                    return False
                counter = 0
            if (nums[j] == 1 or nums[j] == 0) and nums[i] == 0:
                counter += 1
            if nums[j] == 1 and nums[i] == 1 and k >= 1:
                return False
            i += 1
            j += 1
        return True
