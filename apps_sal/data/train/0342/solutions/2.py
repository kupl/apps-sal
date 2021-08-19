class Solution:

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ans = 0
        for (r, row) in enumerate(board):
            for (c, val) in enumerate(row):
                if val == 'X':
                    ans += 1
                    if r and board[r - 1][c] == 'X':
                        ans -= 1
                    elif c and board[r][c - 1] == 'X':
                        ans -= 1
        return ans
