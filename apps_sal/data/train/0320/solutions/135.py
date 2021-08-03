class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op_count = 0

        while not all([v == 0 for v in nums]):
            for i in range(len(nums)):
                odd = nums[i] % 2
                if odd:
                    nums[i] -= 1
                    op_count += 1
                nums[i] //= 2

            op_count += 1

        return max(0, op_count - 1)
