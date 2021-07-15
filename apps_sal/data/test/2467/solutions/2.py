class Solution:
     def combinationSum3(self, k, n):
         """
         :type k: int
         :type n: int
         :rtype: List[List[int]]
         """
 
         res = []
         temp = []
         idx = 1
         self.backtracking(res, temp, n, k, idx)
         
         return res
     
     def backtracking(self, res, temp, n, k, idx):
         if len(temp) == k and n == 0:
             res.append(temp[:])
             return
         
         for i in range(idx, 10):
             temp.append(i)
             self.backtracking(res, temp, n - i, k, i + 1)
             temp.pop()
             

