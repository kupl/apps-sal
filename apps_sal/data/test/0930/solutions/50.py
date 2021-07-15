n, k = map(int, input().split())
mod = 10**9 + 7

m = 4*10**5 + 500

fac = [1] * (m + 1)
facinv = [1] * (m + 1)
for i in range(1, m+1):
    fac[i] = (fac[i-1] * i) % mod
    facinv[i] = (facinv[i-1] * pow(i, -1, mod)) % mod

def nCk(n, k):
    return (fac[n] * facinv[k] * facinv[n-k]) % mod

if k > (n - 2):
    print(nCk(2*n-1, n))
else:
    ans = 0
    for i in range(k+1):
        ans = (ans + nCk(n-1, i) * nCk(n, i)) % mod
    print(ans)
