import numpy as np
import sys


def main():
    input = sys.stdin.readline
    (H, W) = map(int, input().split())
    A = []
    for _ in range(H):
        S = [0 if c == '#' else 1 for c in input().strip()]
        A.append(S)
    A = np.array(A)
    top = np.zeros((H + 1, W), dtype=np.int)
    bottom = np.zeros((H + 1, W), dtype=np.int)
    right = np.zeros((H, W + 1), dtype=np.int)
    left = np.zeros((H, W + 1), dtype=np.int)
    for i in range(1, H + 1):
        top[i] = (top[i - 1] + 1) * A[i - 1]
    for i in range(H - 1, -1, -1):
        bottom[i] = (bottom[i + 1] + 1) * A[i]
    for i in range(1, W + 1):
        right[:, i] = (right[:, i - 1] + 1) * A[:, i - 1]
    for i in range(W - 1, -1, -1):
        left[:, i] = (left[:, i + 1] + 1) * A[:, i]
    R = (top[1:] + bottom[:H] - 1) * A
    C = (right[:, 1:] + left[:, :W] - 1) * A
    RC = (R + C - 1) * A
    return RC.max()


def __starting_point():
    print(main())


__starting_point()
