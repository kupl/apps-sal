import sys
sys.setrecursionlimit(10**9)

n = int(input())
route = [[] for _ in range(n)]
distance = [-1 for _ in range(n)]
INF = float('inf')

for _ in range(n - 1):
    a, b, c = list(map(int, input().split()))
    route[a - 1].append((b - 1, c))
    route[b - 1].append((a - 1, c))
q, k = list(map(int, input().split()))


def Tree(s, g, c):
    distance[s] = c
    for g1, val in route[s]:
        if g == g1:
            continue
        Tree(g1, s, c + val)


def TransitTreePath():
    Tree(k - 1, -1, 0)
    for _ in range(q):
        x, y = list(map(int, input().split()))
        ans = distance[x - 1] + distance[y - 1]
        print(ans)


def __starting_point():
    TransitTreePath()


__starting_point()
