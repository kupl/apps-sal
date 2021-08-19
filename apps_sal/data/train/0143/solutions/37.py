class Solution(object):

    def totalFruit(self, nums):
        d = {}
        k = 2
        maxL = 0
        L = 0
        for R in range(len(nums)):
            if nums[R] in d:
                d[nums[R]] += 1
            else:
                d[nums[R]] = 1
            while len(d) > k:
                d[nums[L]] -= 1
                if d[nums[L]] == 0:
                    del d[nums[L]]
                L += 1
            maxL = max(maxL, R - L + 1)
        return maxL
