class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        a = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                a.append(a[-1] + nums[j] if j != i else nums[i])
        a = sorted(a)
        return sum(a[left - 1:right]) % 1000000007
