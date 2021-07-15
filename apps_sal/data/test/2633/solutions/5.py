class Solution:
     def calculateMinimumHP(self, dungeon):
         """
         :type dungeon: List[List[int]]
         :rtype: int
         """
         num_rows = len(dungeon)
         num_cols = len(dungeon[0])
         INF = float('inf')
         for ri in range(num_rows - 1, -1, -1):
             for ci in range(num_cols - 1, -1, -1):
                 if ri == num_rows - 1 and ci == num_cols - 1:
                     need = -dungeon[ri][ci] + 1
                 else:
                     down = INF if ri == num_rows - 1 else dungeon[ri+1][ci]
                     right = INF if ci == num_cols - 1 else dungeon[ri][ci + 1]
                     need = min(down, right) - dungeon[ri][ci]
                 dungeon[ri][ci] = max(need, 1)
         return dungeon[0][0]

