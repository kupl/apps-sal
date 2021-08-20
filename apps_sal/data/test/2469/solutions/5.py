class Solution:

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n1 = n2 = None
        c1 = c2 = 0
        for i in nums:
            if n1 == i:
                c1 += 1
            elif n2 == i:
                c2 += 1
            elif c1 == 0:
                (n1, c1) = (i, 1)
            elif c2 == 0:
                (n2, c2) = (i, 1)
            else:
                (c1, c2) = (c1 - 1, c2 - 1)
        return [n for n in [n1, n2] if n is not None and nums.count(n) > len(nums) // 3]
