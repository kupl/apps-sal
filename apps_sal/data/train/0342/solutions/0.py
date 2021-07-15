class Solution:
     def countBattleships(self, board):
         """
         :type board: List[List[str]]
         :rtype: int
         """
         count = 0
         for i in range(len(board)):
             for j in range(len(board[i])):
                 if board[i][j] == 'X':
                     if i-1 < 0 and j-1 < 0:
                         count += 1
                     elif i-1 < 0 and board[i][j-1] != 'X':
                         count += 1
                     elif j-1 < 0 and board[i-1][j] != 'X':
                         count += 1
                     elif board[i-1][j] != 'X' and board[i][j-1] != 'X':
                         count += 1
         return count

