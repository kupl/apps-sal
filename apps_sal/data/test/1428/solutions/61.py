# coding: utf-8

# https://atcoder.jp/contests/abc099/tasks
# 15:00-


def main():
    N, C = list(map(int, input().split()))
    D = [None] * C
    for i in range(C):
        D[i] = list(map(int, input().split()))

    c = [None] * N
    for i in range(N):
        c[i] = list(map(int, input().split()))
        c[i] = [x - 1 for x in c[i]]  # 0-index

    STU = [[0] * C, [0] * C, [0] * C]

    for k in range(C):
        for i in range(N):
            for j in range(N):
                STU[(i + j) % 3][k] += D[c[i][j]][k]

    ans = 1000 * N * N
    for i in range(C):

        for j in range(C):
            if j == i:
                continue

            for k in range(C):
                if k == i or k == j:
                    continue
                cand = STU[0][i] + STU[1][j] + STU[2][k]

                if cand < ans:
                    ans = cand

    return ans


print((main()))
