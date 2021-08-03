class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        l = len(digits)
        i = l - 1
        while i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                i -= 1
        if i == -1:
            digits = [1] + digits
        return digits
