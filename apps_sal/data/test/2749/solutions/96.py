import numpy as np


def abc069_d():
    H, W = map(int, input().split())
    _ = int(input())
    A = list(map(int, input().split()))

    flat = []
    for i, a in enumerate(A):
        flat += [i + 1] * a

    grid = np.array(flat, dtype=int).reshape((H, W))
    for i in range(H):
        if i % 2 == 0:
            print(*grid[i], sep=' ')
        else:
            print(*grid[i, ::-1], sep=' ')


abc069_d()
