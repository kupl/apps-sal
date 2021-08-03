class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 not in nums:
            return True
        num_place = nums.index(1)
        f_idx = nums.index(1) + 1

        for i in range(f_idx, len(nums)):
            if nums[i] == 1 and i - num_place < k + 1:

                return False

            elif nums[i] == 1 and i - num_place > k:
                num_place = i

        return True
