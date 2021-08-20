import numpy as np


def main():
    with open(0) as f:
        N = int(f.readline())
        F = np.array([list(map(int, f.readline().split())) for _ in range(N)])
        P = [list(map(int, f.readline().split())) for _ in range(N)]
    max_profit = -np.inf
    for i in range(1, 2 ** 10):
        Open = np.array([i >> j & 1 for j in range(10)])
        conflict = np.dot(F, Open.T)
        profit = sum((P[i][v] for (i, v) in enumerate(conflict)))
        max_profit = max(max_profit, profit)
    print(max_profit)


main()
