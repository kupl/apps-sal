N, K = list(map(int, input().split()))
P = sorted([tuple(map(int, input().split())) for _ in range(N)])

ans = 1e30
for lx in range(N):
    for rx in range(lx+K, N+1):
        Q = sorted(P[lx:rx], key=lambda x:x[1])
        for ly in range(len(Q)):
            R = Q[ly:ly+K]
            if len(R)>=K: ans = min(ans, (P[rx-1][0]-P[lx][0])*(R[-1][1]-R[0][1]))
print(ans)
