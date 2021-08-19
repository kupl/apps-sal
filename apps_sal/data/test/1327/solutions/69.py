import itertools
(N, M) = map(int, input().split())
value = [0] * N
for i in range(N):
    v = list(map(int, input().split()))
    abv = [i if i > 0 else i * -1 for i in v]
    value[i] = v
ans = 0
totals = []
for i in range(0, 2 ** 3):
    totals = []
    for v in range(N):
        tmp = 0
        for j in range(0, 3):
            if i >> j & 1:
                tmp += value[v][j]
            else:
                tmp -= value[v][j]
        totals.append(tmp)
    totals = sorted(totals, reverse=True)
    t = 0
    for k in range(M):
        t += totals[k]
    ans = max(ans, t)
print(ans)
