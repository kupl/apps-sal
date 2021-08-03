class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        digits = list(int(d) for d in str(N))
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                for k in range(i, len(digits)):
                    digits[k] = 9
                digits[i - 1] -= 1

        return int(''.join([str(d) for d in digits]))
