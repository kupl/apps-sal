import sys
readline = sys.stdin.readline
(N, X) = list(map(int, readline().split()))
D = list(map(int, readline().split()))
AD = D + D + [0]
S = [d * (d + 1) // 2 for d in D]
S = S + S + [0]
for i in range(1, 2 * N):
    AD[i] += AD[i - 1]
    S[i] += S[i - 1]
D = D + D + [0]
ans = 0
for r in range(N, 2 * N):
    ng = -1
    ok = r
    while abs(ok - ng) > 1:
        med = (ok + ng) // 2
        if AD[r] - AD[med] < X:
            ok = med
        else:
            ng = med
    l = ok
    res = S[r] - S[l - 1]
    dd = D[l] - (X - (AD[r] - AD[l]))
    res -= dd * (dd + 1) // 2
    ans = max(ans, res)
print(ans)
