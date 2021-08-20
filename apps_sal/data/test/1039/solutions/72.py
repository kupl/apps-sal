import sys
sys.setrecursionlimit(1000000)
N = int(input())
tree = [[] for i in range(N)]
for i in range(N - 1):
    (a, b, c) = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append([b, c])
    tree[b].append([a, c])
(Q, K) = map(int, input().split())
K -= 1
dis = [0] * N


def main(v, p, d):
    dis[v] = d
    for (x, y) in tree[v]:
        if x == p:
            continue
        main(x, v, d + y)


main(K, -1, 0)
for i in range(Q):
    (x, y) = map(int, input().split())
    ans = dis[x - 1] + dis[y - 1]
    print(ans)
