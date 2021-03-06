class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = 0
        output = []
        final_sum = 0
        for i in range(0, len(nums) * (len(nums) + 1) // 2):
            sums = 0
            for k in range(i, len(nums)):
                sums = sums + nums[k]
                output.append(sums)
        output.sort()
        for i in range(left - 1, right):
            final_sum = final_sum + output[i]
        return int(final_sum % (1000000000.0 + 7))
