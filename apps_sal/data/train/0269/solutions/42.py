class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        while sum(nums) >= 2:
            temp = nums.index(1)
            nums[temp] = 0
            if nums.index(1) - temp <= k:
                return False
        return True
