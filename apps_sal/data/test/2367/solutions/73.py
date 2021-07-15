h, w, a, b = list(map(int, input().split()))
m = 10**9 + 7

fac = [1, 1]
inv = [1, 1]
finv = [1, 1]
for i in range(2, w+h+5):
    fac.append(fac[i-1] * i % m)
    inv.append(m - inv[m%i] * (m//i) % m)
    finv.append(finv[i-1] * inv[i] % m)

def nck(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % m) % m


row = []
for i in range(h-a):
    row.append(nck(b+i, i))

ans = 0
for i in range(len(row)-1):
    ans += row[i] * nck(w-b-2 + h-1-i, h-1-i)
    ans %= m

ans += row[-1] * nck(w-b-1 + a, a)
ans %= m

print(ans)

