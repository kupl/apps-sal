import sys
from itertools import permutations

input = sys.stdin.readline


def main():
    N, C = list(map(int, input().split()))
    D = [None] * C
    for i in range(C):
        D[i] = tuple(map(int, input().split()))
    A = [None] * N
    for i in range(N):
        A[i] = tuple(map(int, input().split()))

    R = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            R[(i + j + 2) % 3][A[i][j] - 1] += 1

    cost = [[0] * C for _ in range(3)]
    for r in range(3):
        for Y in range(C):
            tmp = 0
            for X, num in enumerate(R[r]):
                tmp += D[X][Y] * num
            cost[r][Y] = tmp

    ans = float("inf")
    for c0, c1, c2 in permutations(list(range(C)), r=3):
        ans = min(ans, cost[0][c0] + cost[1][c1] + cost[2][c2])

    print(ans)


def __starting_point():
    main()

__starting_point()
