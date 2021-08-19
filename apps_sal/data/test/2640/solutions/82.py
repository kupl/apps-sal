import numpy as np


def main():

    def printl(l):
        return [print(x) for x in l]
    (H, W) = list(map(int, input().split()))
    A = np.array([[1 if i == '.' else 0 for i in input()] for _ in range(H)])
    L = np.zeros((H, W), dtype=np.int)
    R = np.zeros((H, W), dtype=np.int)
    U = np.zeros((H, W), dtype=np.int)
    D = np.zeros((H, W), dtype=np.int)
    L[:, 0] = A[:, 0]
    for w in range(1, W):
        L[:, w] = (L[:, w - 1] + 1) * A[:, w]
    R[:, W - 1] = A[:, W - 1]
    for w in range(W - 2, -1, -1):
        R[:, w] = (R[:, w + 1] + 1) * A[:, w]
    U[0, :] = A[0, :]
    for h in range(1, H):
        U[h, :] = (U[h - 1, :] + 1) * A[h, :]
    D[H - 1, :] = A[H - 1, :]
    for h in range(H - 2, -1, -1):
        D[h, :] = (D[h + 1, :] + 1) * A[h, :]
    print(np.max(L + R + U + D - 3))


def __starting_point():
    main()


__starting_point()
