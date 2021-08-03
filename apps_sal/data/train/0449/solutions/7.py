class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return sorted(nums)[0]
#         low, high = 0, len(nums)-1
#         while low < high:
#             mid = (high - low) / 2
