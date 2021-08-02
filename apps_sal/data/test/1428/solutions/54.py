def LI(): return list(map(int, input().split()))


N, C = LI()
D = [LI() for _ in range(C)]
c = [LI() for _ in range(N)]

INF = 10 ** 15


def main():
    w = [[0] * C for i in range(3)]
    for i in range(N):
        for j in range(N):
            x = (i + j) % 3
            for k in range(C):
                w[x][k] += D[c[i][j] - 1][k]

    ans = INF
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                ans = min(ans, w[0][i] + w[1][j] + w[2][k])
    print(ans)


def __starting_point():
    main()


__starting_point()
