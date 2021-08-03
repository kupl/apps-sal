class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = nums
        for i in range(len(nums) - 1):
            j = i + 1
            while j < n:
                res.append(sum(nums[i:j + 1]))
                j += 1
        return sum(sorted(res)[left - 1:right]) % (10**9 + 7)
