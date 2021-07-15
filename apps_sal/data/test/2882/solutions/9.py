class Solution:
     def generateParenthesis(self, n):
         """
         :type n: int
         :rtype: List[str]
         """
         if not n:
             return []
         cache = [["(", 1, n-1]]
         for _ in range(2*n-1):
             for _ in range(len(cache)):
                 temp = cache.pop(0)
                 if temp[1]:
                     toAdd = temp.copy()
                     toAdd[0] += ')'
                     toAdd[1] -= 1
                     cache.append(toAdd)
                 if temp[2]:
                     temp[0] += '('
                     temp[1] += 1
                     temp[2] -= 1
                     cache.append(temp)
         return [items[0] for items in cache]

