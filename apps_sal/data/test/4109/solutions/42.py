N, M, X = [int(s) for s in input().split()]
Book = [[int(s) for s in input().split()] for _ in range(N)]
INF = 10**7

ans = set()
ans.add(INF)


def DFS(n, cost, Xls):
    if n == N:
        if min(Xls) >= X:
            ans.add(cost)
    else:
        Xnext = [Xls[i] + Book[n][i + 1] for i in range(M)]
        DFS(n + 1, cost + Book[n][0], Xnext)
        DFS(n + 1, cost, Xls)


DFS(0, 0, [0 for _ in range(M)])
if min(ans) == INF:
    print(-1)
else:
    print(min(ans))
