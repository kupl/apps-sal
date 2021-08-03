from itertools import product
import sys
input = sys.stdin.readline


def read():
    X, Y, Z, K = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    C = list(map(int, input().strip().split()))
    return X, Y, Z, K, A, B, C


def solve(X, Y, Z, K, A, B, C, INF=10000000001):
    # 美味しさの上位K=3000件を出力する
    AB = [a + b for a, b in product(A, B)]
    AB.sort(reverse=True)
    AB = AB[:K]
    C.sort(reverse=True)

    D = [AB[k] + C[0] for k in range(len(AB))]
    E = [0 for k in range(len(AB))]
    j = 0
    for k in range(K):
        hi = 0

        # find
        for i in range(len(D)):
            if D[hi] < D[i]:
                hi = i
        # print
        print((D[hi]))

        # update
        E[hi] += 1
        if E[hi] >= len(C):
            D[hi] = -INF
        else:
            D[hi] = AB[hi] + C[E[hi]]


def __starting_point():
    inputs = read()
    solve(*inputs)


__starting_point()
