class Solution:

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '\n         dic = {}\n         for num in nums:\n             if num in dic and dic[num] == 2:\n                 del dic[num]\n             else:\n                 dic[num] = dic.get(num, 0) + 1\n         return [k for k in dic.keys()][0]\n         '
        (one, two) = (0, 0)
        for num in nums:
            (one, two) = (~two & one & ~num | ~two & ~one & num, two & ~one & ~num | ~two & one & num)
        return one
