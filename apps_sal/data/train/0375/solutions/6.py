class Solution(object):

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        (Max, Min) = (max(nums), min(nums))
        if Max == Min:
            return 0
        if len(nums) == 2:
            return Max - Min
        import math
        nums = list(set(nums))
        Len = int(math.ceil((Max - Min) / (len(nums) - 1)))
        print(Max, Min)
        print((Max - Min) / (len(nums) - 1))
        Count = (Max - Min) // Len + 1
        List = [[] for i in range(Count)]
        Gap = 0
        for i in nums:
            ilen = int((i - Min) // Len)
            List[ilen].append(i)
        mmin = max(List[0])
        for i in range(1, Count):
            if List[i] != []:
                Gap = max(Gap, min(List[i]) - mmin)
                mmin = max(List[i])
        return Gap
