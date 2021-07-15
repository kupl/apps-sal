N = int(input())
C = list(map(int,input().split()))
C.sort(reverse=True)
MOD = 10**9+7
if N==1:
    print((C[0]*2)%MOD)
    return

ans = 0
d = pow(2,N-2,MOD)
base = pow(2,N-1,MOD)
for i,c in enumerate(C):
    ans += c * (base + i*d)
ans *= pow(2,N,MOD)
ans %= MOD
print(ans)
