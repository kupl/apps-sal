class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        # zero_ind = -1
        step = 0
        while any(( n > 0 for n in nums)):
            # print('nums', nums)
            if all((n % 2 == 0 for n in nums)):
                nums = [n // 2 for n in nums]
                step += 1
            else:
                # find odd element
                remain_idx = []
                for i, v in enumerate(nums):
                    if v % 2 == 1:
                        nums[i] = nums[i] - 1
                        # if nums[i] == 0:
                        #     zero_ind = max(zero_ind, i)
                        step += 1
                # nums = [ nums[ri] for ri in remain_idx]
        return step
