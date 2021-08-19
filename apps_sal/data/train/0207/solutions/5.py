class Solution:

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        import functools
        nums_str = []
        for each in nums:
            nums_str.append(str(each))
        result = ''.join(sorted(nums_str, key=functools.cmp_to_key(self.comparator)))
        if int(result) == 0:
            return '0'
        else:
            return result

    def comparator(self, a, b):
        num1 = a + b
        num2 = b + a
        if num1 > num2:
            return -1
        elif num2 > num1:
            return 1
        else:
            return 0
