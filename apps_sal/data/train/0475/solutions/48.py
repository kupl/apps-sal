class Solution:

    def rangeSum(self, nums, n, left, right):
        l = []
        mod = 10 ** 9 + 7
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                l.append(sum(nums[i:j + 1]))
        l.sort()
        return sum(l[left - 1:right]) % mod
