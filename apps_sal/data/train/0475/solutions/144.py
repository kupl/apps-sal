class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sum = []
        for i in range(0,len(nums)):
            total_sum = 0
            for k in range(i, len(nums)):
                total_sum += nums[k]
                subarray_sum.append(total_sum)
        subarray_sum.sort()
        return (sum(subarray_sum[left - 1:right]) % (10**9 + 7))
