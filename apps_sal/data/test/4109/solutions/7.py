N, M, X = [int(s) for s in input().split()]
Book = [[int(s) for s in input().split()] for _ in range(N)]
INF = 10**7

ans = set()
ans.add(INF)

for n in range(2**N):
    # Bit全探索
    Xls = [0 for i in range(M)]
    cost = 0
    for i in range(N):
        if ((n >> i) & 1) == 1:
            cost += Book[i][0]
            for b in range(M):
                Xls[b] += Book[i][b + 1]
        if min(Xls) >= X:
            ans.add(cost)
if min(ans) == INF:
    print(-1)
else:
    print(min(ans))
