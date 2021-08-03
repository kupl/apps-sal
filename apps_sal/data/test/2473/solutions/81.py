from collections import defaultdict


def main():
    n, k = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(n)]
    x = [p[0] for p in xy]
    y = [p[1] for p in xy]
    x.sort()
    y.sort()

    s1 = [[0] * n for _ in range(n)]
    s2 = [[0] * n for _ in range(n)]
    s3 = [[0] * n for _ in range(n)]
    s4 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for p in xy:
                if p[0] <= x[i] and p[1] <= y[j]:
                    s1[i][j] += 1
                    s2[i][j] += (p[0] < x[i])
                    s3[i][j] += (p[1] < y[j])
                    s4[i][j] += (p[0] < x[i]) * (p[1] < y[j])
    ans = float('inf')
    for s in range(n):
        for t in range(s + 1, n):
            for u in range(n):
                for v in range(u + 1, n):
                    if s1[t][v] - s3[t][u] - s2[s][v] + s4[s][u] >= k:
                        ans = min(ans, (x[t] - x[s]) * (y[v] - y[u]))
    print(ans)


def __starting_point():
    main()


__starting_point()
