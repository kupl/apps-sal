class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = [
            sum(nums[i:j])
            for i in range(n)
            for j in range(i + 1, n + 1)
        ]
        return sum(sorted(arr)[left - 1:right]) % (10**9 + 7)
