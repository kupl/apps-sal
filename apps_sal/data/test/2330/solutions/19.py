from sys import stdin


def input():
    return stdin.readline().strip()


t = int(input())
for _ in range(t):
    (n, m) = list(map(int, input().split()))
    weight = list(map(int, input().split()))
    edges = [(i, (i + 1) % n) for i in range(n)]
    edges.sort(key=lambda x: weight[x[0]] + weight[x[1]])
    total = sum((weight[u] + weight[v] for (u, v) in edges))
    if m < n:
        print(-1)
    elif n == 2:
        print(-1)
    else:
        (u, v) = edges[0]
        total += (weight[u] + weight[v]) * (m - n)
        print(total)
        for i in range(n):
            print(edges[i][0] + 1, edges[i][1] + 1)
        for j in range(m - n):
            print(edges[0][0] + 1, edges[0][1] + 1)
