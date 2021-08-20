class Solution:

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_dict = {key: 0 for key in nums}
        longest = 0
        for i in nums:
            if length_dict[i]:
                continue
            length = 1
            length_dict[i] = 1
            j = i + 1
            while j in length_dict:
                length_dict[j] = 1
                length += 1
                j += 1
            j = i - 1
            while j in length_dict:
                length_dict[j] = 1
                length += 1
                j -= 1
            longest = max(longest, length)
        return longest
