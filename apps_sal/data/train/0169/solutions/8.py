class Solution:
     def integerBreak(self, n):
         """
         :type n: int
         :rtype: int
         """
         memo = [0] * (59)
         memo[1] = 1
         if n == 2:
             return 1
         if n == 3:
             return 2
         for i in range(2, n + 1):
             tmp = []
             for j in range(1, i):
                 memo[i] = max(i, memo[i], (memo[j] * memo[i - j]))
         return memo[n]

