class Solution:
     def integerBreak(self, n):
         """
         :type n: int
         :rtype: int
         https://leetcode.com/problems/integer-break/discuss/80689/A-simple-explanation-of-the-math-part-and-a-O(n)-solution
         use 3 as many as possible
         """
         if n < 4:
             return n - 1
         ans = 1
         while n > 4:
             ans *= 3
             n -= 3
         ans *= n
         return ans

