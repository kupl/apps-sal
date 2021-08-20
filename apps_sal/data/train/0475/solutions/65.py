class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        mod = math.pow(10, 9) + 7
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sums.append(sum(nums[i:j + 1]))
        return int(sum(sorted(sums)[left - 1:right]) % mod)
