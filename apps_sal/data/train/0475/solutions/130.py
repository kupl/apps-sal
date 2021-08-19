class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sum_list = []
        for i in range(len(nums)):
            sum_list.append(nums[i])
            sums = nums[i]
            for j in range(i + 1, len(nums)):
                sums += nums[j]
                sum_list.append(sums)
        return int(sum(sorted(sum_list)[left - 1:right]) % (10 ** 9 + 7))
