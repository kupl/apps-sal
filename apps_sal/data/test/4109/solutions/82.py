import numpy as np
import itertools


def check():
    N, M, X = map(int, input().split())
    A = np.array([[int(i) for i in input().split()] for _ in range(N)])
    total = np.sum(A, axis=0)
    flag = True if all((a >= X for a in total[1:])) else False
    ans = total[0]

    if flag:
        for i in range(1, N + 1):
            for v in itertools.combinations([i for i in range(N)], i):
                B = np.array([A[j] for j in v])
                total2 = np.sum(B, axis=0)
                sabun = total - total2
                if all(a >= X for a in sabun[1:]):
                    ans = min(ans, sabun[0])
    print(ans if flag else -1)


check()
