class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        sum = 0
        for i in range(0, len(digits)):
            sum = sum * 10 + digits[i]

        return [int(i) for i in str(sum + 1)]
