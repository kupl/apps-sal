import sys
from heapq import heappop, heappush
from scipy.sparse.csgraph import floyd_warshall
input = sys.stdin.readline


def main():
    n, w, l = map(int, input().split())
    d = [[10**15 for _ in range(n)] for _ in range(n)]
    for _ in range(w):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        if z > l:
            continue
        d[x][y] = z
        d[y][x] = z
    for i in range(n):
        d[i][i] = 0
    d = floyd_warshall(d)
    G = [[10**15 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if d[i][j] <= l:
                G[i][j] = 1
                G[j][i] = 1
    for i in range(n):
        G[i][i] = 0
    G = floyd_warshall(G)
    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        ans = G[s][t]
        if ans == 10**15:
            print(-1)
            continue
        print(int(ans) - 1)


def __starting_point():
    main()


__starting_point()
