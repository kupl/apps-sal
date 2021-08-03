class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set_sum = sum(list(set(nums)))
        # set_len = len(set(nums))
        # pro_sum = sum(nums)
        # pro_len = len(nums)
        # return (pro_sum - set_sum) // (pro_len - set_len)

        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        while right - left > 1:
            count = 0
            for num in nums:
                if mid < num <= right:
                    count += 1
            if count > (right - mid):
                left = mid
            else:
                right = mid
            mid = (left + right) // 2
        return right
