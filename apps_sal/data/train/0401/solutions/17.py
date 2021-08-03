class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        snum = sum(nums)
        if not snum % 3:
            return snum
        ones, twos = [], []
        nums.sort()
        for k, v in enumerate(nums):
            if v % 3 == 1:
                ones += [nums[k]]
            if v % 3 == 2:
                twos += [nums[k]]
        if snum % 3 == 1:
            snum = max(snum - ones[0], snum - sum(twos[:2])) if len(twos) >= 2 else snum - ones[0]
        if snum % 3 == 2:
            snum = max(snum - twos[0], snum - sum(ones[:2])) if len(ones) >= 2 else snum - twos[0]
        return snum
