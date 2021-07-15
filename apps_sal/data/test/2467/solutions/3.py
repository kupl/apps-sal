class Solution:
     def combinationSum3(self, k, n):
         res, com = [], []
         self.combination(n, res, com, 1, k)
         return res
     
     def combination(self, target, res, com, begin, k):
         for i in range(begin, target + 1 if target < 9 else 10):
             com.append(i)
             if i == target and k == 1: res.append(com[:])
             self.combination(target - i, res, com, i + 1, k - 1)
             com.pop()

