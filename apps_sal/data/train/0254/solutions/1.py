class Solution:
     def countNumbersWithUniqueDigits(self, n):
         """
         :type n: int
         :rtype: int
         """
         answer = 10 ** n
         for i in range(1, n + 1):
             all_count = 9 * 10 ** (i - 1)
             invalid = 9
             for j in range(1, i):
                 invalid *= (10 - j)
             answer -= (all_count - invalid)
         
         return answer
