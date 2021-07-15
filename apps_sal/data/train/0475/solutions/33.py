class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                sums.append(sum(nums[i:j]))
        sums.sort()
        return sum(sums[left-1:right]) % ((10**9) + 7)
