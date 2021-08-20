N = int(input())
Xs = list(map(int, input().split()))
for (i, x) in enumerate(Xs):
    if i == 0:
        print(Xs[1] - x, Xs[-1] - x)
        continue
    if i == N - 1:
        print(x - Xs[N - 2], x - Xs[0])
        continue
    mincost = min(Xs[i + 1] - x, x - Xs[i - 1])
    maxcost = max(Xs[-1] - x, x - Xs[0])
    print(mincost, maxcost)
