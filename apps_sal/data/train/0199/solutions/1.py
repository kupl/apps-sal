class Solution(object):
    def radix_sort(self, nums):
        if not nums:
            return []
        n_rounds = 0
        num_strs = [str(num) for num in nums]
        n_rounds = max([len(num_str) for num_str in num_strs])
        buckets = [[] for i in range(10)]
        for i in range(n_rounds):
            for num_str in num_strs:
                if i < len(num_str):  # get the last ith digit
                    radix = ord(num_str[-i - 1]) - ord('0')
                else:
                    radix = 0
                buckets[radix].append(num_str)
            num_strs.clear()
            for bucket in buckets:
                num_strs.extend(bucket)
                bucket.clear()
        return [int(num_str) for num_str in num_strs]

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        pos_nums = [num for num in nums if num >= 0]
        neg_nums = [-num for num in nums if num < 0]
        pos_nums = self.radix_sort(pos_nums)
        neg_nums = self.radix_sort(neg_nums)
        nums = [-num for num in reversed(neg_nums)] + pos_nums
        n = 1
        max_n = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                n += 1
                if n > max_n:
                    max_n = n
            elif nums[i] == nums[i - 1]:
                continue
            else:
                n = 1
        return max_n
