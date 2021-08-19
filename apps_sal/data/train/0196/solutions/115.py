class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:

        def max_subarray(nums):
            for i in range(1, len(nums)):
                if nums[i - 1] > 0:
                    nums[i] += nums[i - 1]
            return max(nums)
        (max_sum, cur_sum) = (max_subarray(A[:]), sum(A))
        if max_sum < 0:
            return max_sum
        final_sum = cur_sum + max_subarray(list(map(lambda x: -x, A)))
        return max(max_sum, final_sum)
