import sys
sys.setrecursionlimit(10**7)
N = int(input())

Graph = [[] for _ in range(N + 10)]
dist = [10000000000000] * (N + 10)

for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    Graph[u].append((v, w))
    Graph[v].append((u, w))

dist[0] = 0


def func(fromE, now, length):
    if fromE != -1:
        dist[now] = dist[fromE] + length
    for i in range(len(Graph[now])):
        target = Graph[now][i][0]
        lengt = Graph[now][i][1]

        if target == fromE:
            continue

        func(now, target, lengt)


func(-1, 0, 0)

for i in range(N):
    if dist[i] % 2 == 0:
        print(0)
    else:
        print(1)
