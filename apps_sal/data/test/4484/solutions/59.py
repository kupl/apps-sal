#79 C - Reconciled?
N,M = map(int,input().split())
MOD = 10**9 + 7

if abs(N-M) >= 2:
    ans = 0
else:
    # M! * N!
    Mfact = 1
    for m in range(1,M+1):
        Mfact = (Mfact * m)%MOD
    Nfact = 1
    for n in range(1,N+1):
        Nfact = (Nfact * n)%MOD
    ans = (Nfact*Mfact)%MOD
    if abs(N-M) == 0:
        ans = (ans * 2)%MOD
print(ans)
