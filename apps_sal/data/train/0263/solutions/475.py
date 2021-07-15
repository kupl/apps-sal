class Solution:
    def helper(self, n, board, row, col, cache):
        if n == 0:
            return 1
        
        if (row, col, n) in cache:
            return cache[(row, col, n)]
        
        rows = len(board)
        cols = len(board[0])
        result = 0
        for rMove, cMove in [(-1, -2), (-2, -1), (2, 1), (1, 2), (-2, 1), (1, -2), (2, -1), (-1, 2)]:
            if 0 <= row + rMove < rows and 0 <= col + cMove < cols and board[row+rMove][col+cMove] not in ['*', '#']:
                result += self.helper(n-1, board, row+rMove, col+cMove, cache)
        
        cache[(row, col, n)] = result
        return result
    
    def knightDialer(self, n: int) -> int:
        board = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['*', '0', '#']
        ]
        
        totalResult = 0
        cache = {}
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] not in ['*', '#']:
                    totalResult += self.helper(n-1, board, r, c, cache)
        return totalResult % (10**9 + 7)
