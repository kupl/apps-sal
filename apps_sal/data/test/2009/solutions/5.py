import sys
sys.setrecursionlimit(100000)
N = int(input())
(r1, c1) = list(map(int, input().split()))
(r2, c2) = list(map(int, input().split()))
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1
A = [[int(a) for a in input()] for i in range(N)]
X = [[0] * N for _ in range(N)]
L = []


def dfs(r, c):
    move = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    X[r][c] = 1
    L.append((r, c))
    for m in move:
        (nr, nc) = (r + m[0], c + m[1])
        if nr >= 0 and nr < N and (nc >= 0) and (nc < N):
            if X[nr][nc] == 0 and A[nr][nc] == 0:
                dfs(nr, nc)


dfs(r1, c1)
if X[r2][c2]:
    print(0)
else:
    LL = [l for l in L]
    L = []
    dfs(r2, c2)
    mi = 10 ** 10
    for ll in LL:
        for l in L:
            mi = min((ll[0] - l[0]) ** 2 + (ll[1] - l[1]) ** 2, mi)
    print(mi)
