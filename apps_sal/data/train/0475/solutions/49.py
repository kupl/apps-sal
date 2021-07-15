class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        A = (nums[i:j] for i in range(len(nums)) for j in range(i + 1, len(nums) + 1))
        x = sorted(map(sum, A))
        return sum(x[left - 1:right]) % (10**9 + 7)
