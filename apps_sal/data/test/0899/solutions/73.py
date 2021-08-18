def main():
    from itertools import combinations
    import sys
    input = sys.stdin.readline

    inf = 1000 * 100 + 10

    N, M = list(map(int, input().split()))

    dist = [[[inf, 0] for _ in range(N)] for _ in range(N)]
    for j in range(N):
        dist[j][j] = [0, 0]

    for idx in range(M):
        a, b, c = list(map(int, input().split()))
        a -= 1
        b -= 1
        dist[a][b][0] = dist[b][a][0] = c
        dist[a][b][1] = dist[b][a][1] = 1 << idx

    for k in range(N):
        for i in range(N):
            for j in range(N):
                nd = dist[i][k][0] + dist[k][j][0]
                if dist[i][j][0] > nd:
                    dist[i][j][0] = nd
                    dist[i][j][1] = dist[i][k][1] | dist[k][j][1]
                elif dist[i][j][0] == nd:
                    dist[i][j][1] |= dist[i][k][1] | dist[k][j][1]

    used_edge = 0
    for frm, to in combinations(list(range(N)), r=2):
        used_edge |= dist[frm][to][1]

    print((M - bin(used_edge).count('1')))


def __starting_point():
    main()


__starting_point()
