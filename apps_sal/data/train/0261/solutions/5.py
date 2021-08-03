class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sor = sorted(nums)
        lenn = len(nums)
        return sor[lenn - 1 - (k - 1)]
