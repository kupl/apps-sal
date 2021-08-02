class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if digits[-1] != 9:
            digits[-1] += 1
        else:
            for i in range(-1, -len(digits) - 1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    break
            else:
                digits.insert(0, 1)

        return digits
