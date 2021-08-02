import numpy as np


def main():
    w, h, n = list(map(int, input().split()))
    xyas = [list(map(int, input().split())) for _ in range(n)]
    board = np.array([[0 for i in range(w)] for j in range(h)])
    for x, y, a in xyas:
        if a == 1:
            board[:, :x] = 1
        elif a == 2:
            board[:, x:] = 1
        elif a == 3:
            board[-y:, :] = 1
        elif a == 4:
            board[:-y, :] = 1
    ans = (w * h) - np.sum(board)
    print(ans)


def __starting_point():
    main()


__starting_point()
