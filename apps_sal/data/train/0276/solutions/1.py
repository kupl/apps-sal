class Solution:
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        return self.use_dfs(board, hand)

    def use_dfs(self, board, hand):
        counts = collections.Counter(hand)
        return self.dfs(board, counts)

    def dfs(self, board, hand):
        if not board:
            return 0
        result = float('inf')
        i, j = 0, 0
        n = len(board)
        while i < n:
            j = i
            while j < n and board[i] == board[j]:
                j += 1
            color = board[i]
            insert = 3 - (j - i)
            if color in hand and hand[color] >= insert:
                new_board = self.shrink(board[:i] + board[j:])
                hand[color] -= insert
                dist = self.dfs(new_board, hand)
                if dist >= 0:
                    result = min(result, dist + insert)
                hand[color] += insert
            i = j
        return result if float('inf') != result else -1

    def shrink(self, board):
        i, j = 0, 0
        while i < len(board):
            j = i
            while j < len(board) and board[i] == board[j]:
                j += 1
            if j - i >= 3:
                board = board[:i] + board[j:]
                i = 0
            else:
                i = j
        return board
