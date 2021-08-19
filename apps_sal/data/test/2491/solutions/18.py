def bellman_ford():
    (n, m) = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for i in range(m):
        (a, b, c) = list(map(int, input().split()))
        g[a - 1].append([b - 1, -1 * c])
    dist = [float('inf')] * n
    inf = float('inf')
    dist[0] = 0
    for i in range(n):
        for v in range(n):
            for k in range(len(g[v])):
                edge = g[v][k]
                if dist[v] != inf and dist[v] + edge[1] < dist[edge[0]]:
                    dist[edge[0]] = dist[v] + edge[1]
    ans = dist[n - 1]
    neg = [0] * n
    for i in range(n):
        for edge in g[i]:
            if dist[i] == inf:
                continue
            if dist[i] + edge[1] < dist[edge[0]]:
                dist[edge[0]] = dist[i] + edge[1]
                neg[edge[0]] = 1
            if neg[i]:
                neg[edge[0]] = 1
    if not neg[n - 1]:
        print(dist[n - 1] * -1)
    else:
        print('inf')
    return False


def main():
    bellman_ford()


def __starting_point():
    main()


__starting_point()
