class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for i in range(len(nums)):
            arr.extend(accumulate(nums[i:]))
        arr.sort()
        return sum(arr[left - 1:right]) % (10**9 + 7)
