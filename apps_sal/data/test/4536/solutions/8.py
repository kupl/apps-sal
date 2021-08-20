class Solution:

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            print(i)
            if digits[i] + carry == 10:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits.insert(0, 1)
        return digits
