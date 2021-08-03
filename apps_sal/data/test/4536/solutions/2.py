class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        carry = 1
        while carry != 0 or i >= 0:
            temp = digits[i] + carry
            digits[i] = temp % 10
            carry = temp // 10
            i -= 1
            if i < 0 and carry > 0:
                digits.insert(0, carry)
                carry = 0
        return digits
