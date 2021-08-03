class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cum_sum_dict = {}
        cum_sum_dict[0] = 1
        left_sum = 0
        count = 0
        for t in nums:
            left_sum = left_sum + t
            if (left_sum - k) in cum_sum_dict:
                count = count + cum_sum_dict[left_sum - k]
            if left_sum in cum_sum_dict:
                cum_sum_dict[left_sum] = cum_sum_dict[left_sum] + 1
            else:
                cum_sum_dict[left_sum] = 1

        return count
