class Solution:

    def majorityElement(self, nums):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        l = []
        for i in list(d.keys()):
            if d[i] > len(nums) // 3:
                l.append(i)
        return l
