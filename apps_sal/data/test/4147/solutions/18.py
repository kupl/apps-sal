import sys
from itertools import product

input = sys.stdin.readline


def main():
    N, A, B, C = list(map(int, input().split()))
    L = [0] * N
    for i in range(N):
        L[i] = int(input())

    ans = float("inf")
    for comb in product(list(range(4)), repeat=N):
        mp = -30
        a = b = c = 0
        for i, j in enumerate(comb):
            if j == 0:
                continue
            elif j == 1:
                a += L[i]
            elif j == 2:
                b += L[i]
            elif j == 3:
                c += L[i]
            mp += 10

        if min(a, b, c) == 0:
            continue

        mp += abs(A - a) + abs(B - b) + abs(C - c)
        if mp < ans:
            ans = mp

    print(ans)


def __starting_point():
    main()


__starting_point()
