class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        num = len(nums) - 1
        for i in range(len(nums)):
            x = 0
            for j in range(i, i + num + 1):
                x += nums[j]
                sums.append(x)
            num -= 1
        sums.sort()
        return sum(sums[left - 1:right]) % (10 ** 9 + 7)
