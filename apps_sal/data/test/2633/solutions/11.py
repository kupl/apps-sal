class Solution:
     def calculateMinimumHP(self, dungeon):
         """
         :type dungeon: List[List[int]]
         :rtype: int
         """
         if not any(dungeon):
             return 1
         m = len(dungeon)
         n = len(dungeon[0])
         memo = {(m - 1, n - 1): 1}
         def helper(i, j):
             if (i, j) not in memo:
                 if i == m - 1:
                     ans = max(1, helper(i, j+1) - dungeon[i][j+1])
                 elif j == n - 1:
                     ans = max(1, helper(i+1, j) - dungeon[i+1][j])
                 else:
                     ans = min(max(1, helper(i, j+1) - dungeon[i][j+1]),
                              max(1, helper(i+1, j) - dungeon[i+1][j]))
                 memo[(i, j)] = ans
             return memo[(i, j)]
         return max(1, helper(0, 0) - dungeon[0][0])
         

