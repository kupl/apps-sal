class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        try:
            last = nums.index(1)
        except:
            return True

        for i in range(last + 1, len(nums)):
            if nums[i] == 1 and i - last <= k:
                return False
            elif nums[i] == 1:
                last = i

        return True
