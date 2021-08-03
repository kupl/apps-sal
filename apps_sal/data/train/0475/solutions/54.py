class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 1000000007
        s = [sum(nums[i:i + j]) for i in range(0, len(nums)) for j in range(1, len(nums) - i + 1)]

        sorted_s = sorted(s)

        return sum(sorted_s[left - 1: right]) % MOD
