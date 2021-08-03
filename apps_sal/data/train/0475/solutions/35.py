class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                res.append(sum(nums[i:j]))
        res.sort()
        return sum(res[left - 1:right]) % (10**9 + 7)
