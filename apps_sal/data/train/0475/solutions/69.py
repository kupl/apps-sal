from itertools import accumulate
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result = []
        for i in range(n):
            result.extend(list(accumulate(nums[i:])))
        result.sort()
        return sum(result[left-1:right]) % (10**9+7)

