class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                k = sum(nums[i:j + 1])
                res.append(k)
        res.sort()

        return sum(res[left - 1:right]) % (10**9 + 7)
