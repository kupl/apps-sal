import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())
l = [-1] * N
tree = [[] for i in range(N)]
for i in range(N - 1):
    A, B, C = list(map(int, input().split()))
    A -= 1
    B -= 1
    tree[A].append((B, C))
    tree[B].append((A, C))
Q, V = list(map(int, input().split()))


def DFS(now, past, dis):
    l[now] = dis
    for i in tree[now]:
        if i[0] == past:
            continue
        elif l[i[0]] == -1:
            DFS(i[0], now, dis + i[1])


DFS(V - 1, -1, 0)
for i in range(Q):
    s, e = list(map(int, input().split()))
    s -= 1
    e -= 1
    print(l[s] + l[e])
