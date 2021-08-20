class Solution:

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        tails = [nums[0]]
        for i in range(1, n):
            x = nums[i]
            (l, r) = (0, len(tails) - 1)
            while l < r:
                mid = (l + r) // 2
                if tails[mid] >= x:
                    r = mid
                else:
                    l = mid + 1
            if tails[l] < x:
                tails.append(x)
            else:
                tails[l] = x
        return len(tails)
