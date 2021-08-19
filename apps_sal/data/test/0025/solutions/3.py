import sys


def solve():
    (n, k) = map(int, input().split())
    if k > n ** 2:
        print(-1)
    else:
        mat = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(i, n):
                if k <= 0:
                    break
                if i == j:
                    mat[i][i] = 1
                    k -= 1
                elif k > 1:
                    mat[i][j] = mat[j][i] = 1
                    k -= 2
        for mat_r in mat:
            print(*mat_r)


def __starting_point():
    solve()


__starting_point()
