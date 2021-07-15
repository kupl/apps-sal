# MOD下での階乗とその逆元を求める関数
# O(nlogn + n) ?
def prepare(n):
    nonlocal mod
    modFacts = [0] * (n + 1)
    modFacts[0] = 1
    for i in range(n):
        modFacts[i + 1] = (modFacts[i] * (i + 1)) % mod

    invs = [1] * (n + 1)
    invs[n] = pow(modFacts[n], mod - 2, mod)
    for i in range(n, 1, -1):
        invs[i - 1] = (invs[i] * i) % mod

    return modFacts, invs

n,m = list(map(int,input().split()))
mod = 10**9+7
modFacts,invs = prepare(m)
ans = 0
nci = 0
for i in range(n+1):
    nci = (modFacts[n]*invs[n-i]*invs[i]) % mod
    mpi = (modFacts[m]*invs[m-i]) % mod
    mipni = (modFacts[m-i]*invs[m-n]) % mod
    ans += ((nci * mpi * mipni**2) % mod )* (-1)**i
    ans %= mod
    # print(i,nci,mpi,mipni)
print(ans)

