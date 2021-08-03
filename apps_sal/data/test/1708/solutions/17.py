def inpl(): return list(map(int, input().split()))


N, M = inpl()
A = inpl()
C = inpl()
Dishnum = sum(A)
ACi = [[c, i, a] for i, (a, c) in enumerate(zip(A, C), 1)]
ACi.sort()
Orig = dict()
for i, (_, j, _) in enumerate(ACi):
    Orig[j] = i
ctr = 0
for _ in range(M):
    ans = 0
    t, d = inpl()
    t = Orig[t]
    Dishnum -= d
    if Dishnum < 0:
        print(ans)
        continue
    k = min(d, ACi[t][2])
    ACi[t][2] -= k
    d -= k
    ans += k * ACi[t][0]
    while d > 0:
        k = min(d, ACi[ctr][2])
        ACi[ctr][2] -= k
        d -= k
        ans += k * ACi[ctr][0]
        if not ACi[ctr][2]:
            ctr += 1
    print(ans)
