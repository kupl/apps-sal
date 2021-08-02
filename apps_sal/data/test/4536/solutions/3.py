class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = [str(i) for i in digits]
        l = int(''.join(l))
        l += 1
        l = list(str(l))
        l = [int(i) for i in l]
        return l
