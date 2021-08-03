class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = dict()
        results = []
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] > len(nums) // 3:
                if num not in results:
                    results.append(num)
        return results
