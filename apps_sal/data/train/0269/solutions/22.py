class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        s = -1
        for i in range(len(nums)):
            if nums[i] == 1 and s == -1:
                s = i
            elif nums[i] == 1 and i-s <= k:
                return False
            elif nums[i] == 1 and i-s > k:
                s = i
        return True
