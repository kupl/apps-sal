class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for L in range(len(nums)):
            R = len(nums)
            while L < R:
                sums.append(sum(nums[L:R]))
                R -= 1
        sums.sort()
        return sum(sums[left - 1:right]) % (10 ** 9 + 7)
