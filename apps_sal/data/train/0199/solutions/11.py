class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_set = set(nums)
        for num in list(nums_set):
            if num - 1 not in nums_set and num + 1 not in nums_set:
                nums_set.remove(num)
        max_group_size = 1
        while nums_set:
            num = nums_set.pop()
            group_size = 1
            prev_num = num - 1
            while prev_num in nums_set:
                group_size += 1
                nums_set.remove(prev_num)
                prev_num -= 1
            next_num = num + 1
            while next_num in nums_set:
                group_size += 1
                nums_set.remove(next_num)
                next_num += 1
            if group_size > max_group_size:
                max_group_size = group_size
        return max_group_size
