class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
         count frequency of each element
         """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, frequency in list(freq.items()):
            if frequency == 1:
                return num
