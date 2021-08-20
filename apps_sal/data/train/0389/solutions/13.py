class Solution:

    def splitArraySameAverage(self, nums):

        def find(target, k, i):
            if (target, k) in d and d[target, k] <= i:
                return False
            if k == 0:
                return target == 0
            if k + i > len(nums):
                return False
            res = find(target - nums[i], k - 1, i + 1) or find(target, k, i + 1)
            if not res:
                d[target, k] = min(d.get((target, k), length), i)
            return res
        (d, length, sum_nums) = ({}, len(nums), sum(nums))
        return any((find(sum_nums * i // length, i, 0) for i in range(1, length // 2 + 1) if sum_nums * i % length == 0))
