import sys
from itertools import product

input = sys.stdin.readline


def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    H = [0] * N
    for i in range(N):
        X[i], Y[i], H[i] = list(map(int, input().split()))

    for Cx, Cy in product(list(range(101)), repeat=2):
        Ch = set()
        Ch_upper = float("inf")
        for x, y, h in zip(X, Y, H):
            a = abs(x - Cx) + abs(y - Cy)
            if h == 0:
                Ch_upper = min(Ch_upper, a)
            else:
                Ch.add(h + a)
        if len(Ch) != 1:
            continue
        else:
            Ch = Ch.pop()
            if Ch <= Ch_upper:
                ans = f"{Cx} {Cy} {Ch}"
                break

    print(ans)


def __starting_point():
    main()


__starting_point()
