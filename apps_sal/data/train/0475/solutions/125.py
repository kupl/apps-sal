class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(n):
            rollingSum = 0
            for j in range(i, n):
                rollingSum += nums[j]
                sums.append(rollingSum)
        sums.sort()
        prefixSum = 0
        for i in range(left - 1, right):
            prefixSum += sums[i]
        return prefixSum % (10 ** 9 + 7)
