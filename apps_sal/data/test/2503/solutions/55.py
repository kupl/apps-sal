import numpy as np


def imos2d(x1, y1, x2, y2, board):
    board[y1][x1] += 1
    board[y2][x2] += 1
    board[y2][x1] -= 1
    board[y1][x2] -= 1


def __starting_point():
    N, K = list(map(int, input().split()))
    lines = [input() for _ in range(N)]

    K2 = 2 * K
    add_dict = {"W": 0, "B": K}
    board = [[0 for _ in range(K2 + 1)] for _ in range(K2 + 1)]
    for line in lines:
        ls = line.split()
        x = int(ls[0]) % K2
        y = (int(ls[1]) + add_dict[ls[2]]) % K2
        x_ = x % K
        y_ = y % K

        # 左上・右上・中央・左下・右下
        if (x < K and y < K) or (K <= x and K <= y):
            # 左上
            imos2d(0, 0, x_ + 1, y_ + 1, board)
            # 右上
            imos2d(x_ + K + 1, 0, K2, y_ + 1, board)
            # 左下
            imos2d(0, y_ + K + 1, x_ + 1, K2, board)
            # 右下
            imos2d(x_ + K + 1, y_ + K + 1, K2, K2, board)
            # 中央
            imos2d(x_ + 1, y_ + 1, x_ + K + 1, y_ + K + 1, board)
        # 上・下・左・右
        else:
            # 上
            imos2d(x_ + 1, 0, x_ + K + 1, y_ + 1, board)
            # 下
            imos2d(x_ + 1, y_ + K + 1, x_ + K + 1, K2, board)

            # 左
            imos2d(0, y_ + 1, x_ + 1, y_ + K + 1, board)
            imos2d(x_ + K + 1, y_ + 1, K2, y_ + K + 1, board)

    board = np.array(board)
    for x in range(K2):
        board[:, x + 1] += board[:, x]
    for y in range(K2):
        board[y + 1, :] += board[y, :]

    print((board.max()))


__starting_point()
