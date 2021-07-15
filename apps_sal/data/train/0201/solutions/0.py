class Solution:
     hash = {}
     def numTrees(self, n):
         """
         :type n: int
         :rtype: int
         """
         # return base case
         if n == 0:
             return 1
         if n == 1 or n == 2:
             return n
         
         # try fetching from hash
         try:
             return self.hash[n]
         except KeyError:
             pass
         
         # holds the sum
         resSum = 0
         
         # iterate i from 1 to n-1
         # should add up (0,4), (1,3), (2,2), (3,1), (4,0)
         for i in range(n):
             #print(i,n - (i+1))
             tempSum = self.numTrees(i) * self.numTrees(n - (i+1))
             #print(tempSum)
             resSum += tempSum
             
         # append to hash
         self.hash[n]=resSum
         return resSum
