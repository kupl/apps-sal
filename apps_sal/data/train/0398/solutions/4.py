class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_map = {0: 1}
        count = 0
        total_sum = 0
        total = 0
        for numb in nums:
            total += numb
            count += sum_map.get(total - k, 0)
            sum_map[total] = sum_map.get(total, 0) + 1
        return count
