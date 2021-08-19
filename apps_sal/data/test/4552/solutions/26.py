import sys
from itertools import product
input = sys.stdin.readline


def main():
    N = int(input())
    F = [None] * N
    for i in range(N):
        F[i] = tuple(map(int, input().split()))
    P = [None] * N
    for i in range(N):
        P[i] = tuple(map(int, input().split()))
    ans = -float('inf')
    for comb in product(list(range(2)), repeat=10):
        if sum(comb) == 0:
            continue
        c = [0] * N
        for (j, is_open) in enumerate(comb):
            if is_open:
                for i in range(N):
                    c[i] += F[i][j]
        profit = sum((P[i][c[i]] for i in range(N)))
        ans = max(ans, profit)
    print(ans)


def __starting_point():
    main()


__starting_point()
