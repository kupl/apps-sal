class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l, r = 0, nums[-1] - nums[0]

        while l < r:
            m = l + (r - l) // 2
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > m:
                    left += 1
                count += (right - left)
            if count < k:
                l = m + 1
            else:
                r = m
        return l
