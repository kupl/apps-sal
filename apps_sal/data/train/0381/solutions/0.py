class Solution:

    def minSubArrayLen(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        _min = float('inf')
        _sum = 0
        j = 0
        for (i, n) in enumerate(nums):
            _sum += n
            while _sum >= k:
                _min = min(i - j + 1, _min)
                _sum -= nums[j]
                j += 1
        return _min if _min != float('inf') else 0
