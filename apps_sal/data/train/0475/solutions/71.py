from itertools import accumulate


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        data = []
        for i in range(len(nums)):
            data.extend(accumulate(nums[i:]))
        data.sort()
        return sum(data[left - 1:right]) % (10**9 + 7)
