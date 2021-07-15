class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1 and nums[0] % 3:
            return 0

        sum_ = sum(nums)
        mod_ = sum_ % 3
        if not mod_:
            return sum_

        vals = {False: self.min_two([n for n in nums if n % 3 == 3 - mod_]),
                True: [min([n for n in nums if n % 3 == mod_])]}

        if vals[True] and (len(vals[False]) <= 1 or vals[True][0] < sum(vals[False])):
            return sum_ - vals[True][0]

        elif len(vals[False]) == 2:
            return sum_ - sum(vals[False])
        return 0



    def min_two(self, l):
        if not l:
            return []
        idx = [i for i in range(len(l))]
        out = [min(idx, key = lambda i: l[i])]
        idx.pop(out[0])
        if idx:
            out.append(min(idx, key = lambda i: l[i]))

        return [l[i] for i in out]
