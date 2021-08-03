class Solution:
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        res = float("inf")
        hmap = collections.defaultdict(int)
        for c in hand:
            hmap[c] += 1
        res = self.helper(board, hmap)
        if res == float("inf"):
            return -1
        return res

    def helper(self, board, hmap):
        board = self.removeConsecutive(board)
        if len(board) == 0:
            return 0
        cnt = float("inf")
        j = 0
        for i in range(len(board) + 1):
            if i < len(board) and board[i] == board[j]:
                continue
            need = 3 - (i - j)
            if hmap[board[j]] >= need:
                hmap[board[j]] -= need
                res = self.helper(board[0:j] + board[i:], hmap)
                if res != float("inf"):
                    cnt = min(cnt, res + need)
                hmap[board[j]] += need
            j = i
        return cnt

    def removeConsecutive(self, board):
        j = 0
        for i in range(len(board) + 1):
            if i < len(board) and board[i] == board[j]:
                continue
            if i - j >= 3:
                return self.removeConsecutive(board[0:j] + board[i:])
            else:
                j = i
        return board
