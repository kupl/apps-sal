class Solution:
     def canCross(self, stones):
         """
         :type stones: List[int]
         :rtype: bool
         """
         queue, target = [(0, 0)], stones[-1]
         invalid, stones = set(), set(stones)
         while queue:
             pos, jump = queue.pop()
             for n in (jump-1, jump, jump+1):
                 if n > 0:
                     if pos + n == target:
                         return True
                     elif pos + n in stones and (pos + n, n) not in invalid:
                         queue += [(pos+n, n)]
             invalid.add((pos, jump))
         return False
     
         # stone_set, fail = set(stones), set()
         # stack = [(0, 0)]
         # while stack:
         #     stone, jump = stack.pop()
         #     for j in (jump-1, jump, jump+1):
         #         s = stone + j
         #         if j > 0 and s in stone_set and (s, j) not in fail:
         #             if s == stones[-1]:
         #                 return True
         #             stack.append((s, j))
         #     fail.add((stone, jump))
         # return False
     
         
                 

