class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarr = [sum(nums[i:i+j]) for i in range(0,len(nums)) for j in range(1,len(nums)-i+1)]
        subarr = sorted(subarr)
        return sum(subarr[left-1:right])%(10**9+7)
