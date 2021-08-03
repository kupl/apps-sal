import numpy as np


def main():
    h, w = map(int, input().split())
    s = np.array([list(input()) for _ in range(h)])
    t = np.zeros((h + 2, w + 2))
    t[1:-1, 1:-1][s == "."] = 1
    row = np.zeros((h + 2, w + 2))
    col = np.zeros((w + 2, h + 2))
    for i in range(1, h + 1):
        idx = np.where(t[i] == 0)[0]
        dif = np.diff(idx)
        row[i, idx[:-1] + 1] += dif - 1
        row[i, idx[1:]] -= dif - 1
        row[i] = np.cumsum(row[i])
    t = t.T
    for i in range(1, w + 1):
        idx = np.where(t[i] == 0)[0]
        dif = np.diff(idx)
        col[i, idx[:-1]] += dif - 2
        col[i, idx[1:]] -= dif - 2
        col[i] = np.cumsum(col[i])
    col = col.T
    cost = np.add(row, col)
    print(int(np.max(cost)))


def __starting_point():
    main()


__starting_point()
