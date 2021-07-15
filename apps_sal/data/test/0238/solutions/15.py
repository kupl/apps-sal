N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))
bv = 0
for ms in range(M):
    cv = 0
    for i in range(ms, N):
        v = A[i]
        if i % M == ms:
            v -= K
            cv = max(0, cv)
        cv += v
        bv = max(bv, cv)
print(bv)

