class Solution:

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d = [str(x) for x in digits]
        num = int(''.join(d)) + 1
        return list(map(int, str(num)))
