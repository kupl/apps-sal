class Solution:

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _dict = {}
        for num in nums:
            if num not in _dict:
                _dict[num] = 1
            elif _dict[num] == 1:
                _dict[num] += 1
            else:
                del _dict[num]
        return list(_dict.keys())[0]
