import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(a) for a in input().split()] + [0] * 5
    X = [0] + [1 << 30] * (N + 5)
    for i in range(2, N + 5):
        X[i] = min(X[i], X[i - 2] + A[i - 2])
        if i >= 3:
            X[i] = min(X[i], X[i - 3] + A[i - 3])
        if i >= 4:
            X[i] = min(X[i], X[i - 4] + A[i - 4] + A[i - 3])
    print(min(X[-5:]))
