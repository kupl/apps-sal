class Solution:
    def minOperations(self, nums: List[int]) -> int:

        def all_zeros(nums):
            for num in nums:
                if num != 0:
                    return False
            return True

        def to_all_evens(nums):
            cnt = 0
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    cnt += 1
                    nums[i] -= 1
            return cnt

        op_cnt = 0
        while not all_zeros(nums):
            op_cnt += to_all_evens(nums)
            if not all_zeros(nums):
                nums = [x // 2 for x in nums]
                op_cnt += 1
        return op_cnt
