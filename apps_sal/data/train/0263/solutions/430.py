class Solution:
    def knightDialer(self, n: int) -> int:
        # https://blog.csdn.net/fuxuemingzhu/article/details/83716573
        self.ans = dict()
        self.ans[0] = 10
        board = [[1] * 3 for _ in range(4)]
        board[3][0] = board[3][2] = 0
        pre_dict = {(i, j): self.prevMove(i, j) for i in range(4) for j in range(3)}
        for n in range(1, n):
            new_board = copy.deepcopy(board)
            for i in range(4):
                for j in range(3):
                    cur_move = 0
                    for x, y in pre_dict[(i, j)]:
                        cur_move = (cur_move + board[x][y]) % (10 ** 9 + 7)
                    new_board[i][j] = cur_move
            board = new_board
        return sum([board[i][j] for i in range(4) for j in range(3)]) % (10 ** 9 + 7)

    def prevMove(self, i, j):
        if (i, j) == (3, 0) or (i, j) == (3, 2):
            return []
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        res = []
        for d in directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < 4 and 0 <= y < 3 and (x, y) != (3, 0) and (x, y) != (3, 2):
                res.append((x, y))
        return res
