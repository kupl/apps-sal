def main():
    import sys
    input = sys.stdin.readline
    inf = 1000 * 100 + 10
    (N, M) = list(map(int, input().split()))
    dist = [[inf for _ in range(N)] for _ in range(N)]
    for j in range(N):
        dist[j][j] = 0
    es = []
    for _ in range(M):
        (a, b, c) = list(map(int, input().split()))
        a -= 1
        b -= 1
        es.append((a, b, c))
        dist[a][b] = dist[b][a] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d = dist[i][k] + dist[k][j]
                if dist[i][j] > d:
                    dist[i][j] = d
    ans = 0
    for (a, b, c) in es:
        if dist[a][b] == c:
            continue
        ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
