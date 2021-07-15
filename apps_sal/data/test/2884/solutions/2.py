class Solution:
     def combinationSum2(self, candidates, target):
         """
         :type candidates: List[int]
         :type target: int
         :rtype: List[List[int]]
         """
         if not candidates:
             return []
         result = []
         candidates.sort()
         self.dfs(result, [], 0, target, candidates)
         return result
     
     def dfs(self, result, combin, start, target, candidates):
         if target == 0:
             result.append([i for i in combin])
         else:
             for index in range(start, len(candidates)):
                 if candidates[index] > target:
                     break
                 if (index > start and candidates[index] == candidates[index - 1]):
                     continue
                 combin.append(candidates[index])
                 self.dfs(result, combin, index + 1, target - candidates[index], candidates)
                 combin.pop()

