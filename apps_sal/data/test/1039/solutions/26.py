import sys
sys.setrecursionlimit(10 ** 7)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(MAP())
def NIJIGEN(H): return [list(input()) for i in range(H)]


def bfs(place, dis):
    for i in tree[place]:
        a, b = i
        if a not in finish:
            finish.add(a)
            disli[a] = dis + b
            bfs(a, dis + b)


N = INT()
tree = [[] for _ in range(N)]
for i in range(N - 1):
    a, b, c = MAP()
    tree[a - 1].append([b - 1, c])
    tree[b - 1].append([a - 1, c])
Q, K = MAP()
disli = [0 for i in range(N)]
finish = set([K - 1])
bfs(K - 1, 0)
for i in range(Q):
    a, b = MAP()
    print(disli[a - 1] + disli[b - 1])
