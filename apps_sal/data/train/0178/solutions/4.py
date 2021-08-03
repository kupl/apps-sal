class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tails = [0] * (len(nums))
        size = 0
        for num in nums:
            i = 0
            j = size
            while i != j:
                mid = (i + j) // 2
                if tails[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            tails[j] = num
            size = max(i + 1, size)
        return size
