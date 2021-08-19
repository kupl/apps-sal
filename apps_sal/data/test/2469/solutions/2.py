class Solution:

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        l = len(nums)
        candidate1 = candidate2 = 0
        count1 = count2 = 0
        for i in nums:
            if candidate1 == i:
                count1 += 1
            elif candidate2 == i:
                count2 += 1
            elif count1 == 0:
                candidate1 = i
                count1 = 1
            elif count2 == 0:
                candidate2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        c1 = nums.count(candidate1)
        c2 = nums.count(candidate2)
        res = []
        if c1 > l / 3:
            res.append(candidate1)
        if c2 > l / 3 and candidate1 != candidate2:
            res.append(candidate2)
        return res
