class Solution(object):

    def twoSum(self, nums, target):
        hashdict = {}
        for (i, num) in enumerate(nums):
            if target - num in hashdict:
                return [hashdict[target - num], i]
            else:
                hashdict[num] = i
