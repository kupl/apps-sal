from itertools import permutations
import sys
input = sys.stdin.readline


def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    grid = [list(map(int, input().split())) for _ in range(N)]

    sup0 = [0] * C
    sup1 = [0] * C
    sup2 = [0] * C
    for i in range(N):
        for j in range(N):
            if (i + j) % 3 == 0:
                sup2[grid[i][j] - 1] += 1
            elif (i + j) % 3 == 1:
                sup0[grid[i][j] - 1] += 1
            elif (i + j) % 3 == 2:
                sup1[grid[i][j] - 1] += 1

    ans = 10 ** 18
    for i, j, k in permutations(range(C), 3):
        tmp = 0
        for c in range(C):
            tmp += D[c][i] * sup0[c]
            tmp += D[c][j] * sup1[c]
            tmp += D[c][k] * sup2[c]
        ans = min(ans, tmp)
    print(ans)


def __starting_point():
    main()


__starting_point()
