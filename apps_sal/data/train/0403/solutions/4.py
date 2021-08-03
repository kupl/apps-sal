class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return False
        forward = [nums[0]] * n
        backward = [nums[-1]] * n
        for i in range(1, n):
            forward[i] = min(forward[i - 1], nums[i])
        for i in range(n - 2, -1, -1):
            backward[i] = max(backward[i + 1], nums[i])
        for i in range(n):
            if forward[i] < nums[i] < backward[i]:
                return True
        return False
