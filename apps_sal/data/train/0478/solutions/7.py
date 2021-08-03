class Solution:
    def singleNumber(self, nums):
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1
        for i in list(dict.keys()):
            if dict[i] == 1:
                return i
        return -1
