class Solution:

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = {}
        for i in nums:
            if str(i) not in res:
                res[str(i)] = 1
            else:
                res[str(i)] += 1
        for i in res:
            if res[i] == 1:
                return int(i)
