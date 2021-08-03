class Solution:
    def minOperations(self, nums):
        ret = []
        overall = 0
        for i in nums:
            temp = 0
            if i == 0:
                overall -= 1
            if i % 2 == 1 and i != 1:
                overall += 1
                i -= 1
            while i > 1:
                if i % 2 == 1:
                    overall += 1
                    i -= 1
                else:
                    temp += 1
                    i /= 2
            ret.append(temp)
        return (overall + max(ret) + len(ret))
