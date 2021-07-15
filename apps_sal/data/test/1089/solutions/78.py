MOD = 10**9+7

# フェルマーの小定理
def nCr(n, r, mod=10**9+7):
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod

N, M, K = list(map(int, input().split()))
ans = 0
# 2点の差がxになる組み合わせは同じ行でM-x通り、2点の行の組み合わせはN*N通り
for x in range(M):
    ans += x * (M-x) * N*N
for y in range(N):
    ans += y * (N-y) * M*M

# 2点以外(K-2)をN*M-2のマスに配置する組み合わせはnCr(N*M-2, K-2)通り
ans *= nCr(N*M-2, K-2, MOD)
ans %= MOD

print(ans)

