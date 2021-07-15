class Solution:
     def monotoneIncreasingDigits(self, N):
         """
         :type N: int
         :rtype: int
         """
         digits = list(map(int, str(N)))
         i = 0
         while i < len(digits) - 1 and digits[i] <= digits[i+1]:
             i += 1
         while 0 <= i < len(digits) - 1 and digits[i] > digits[i+1]:
             digits[i] -= 1
             i -= 1
         digits[i+2:] = '9' * (len(digits) - i - 2)
         return int(''.join(map(str, digits)))

