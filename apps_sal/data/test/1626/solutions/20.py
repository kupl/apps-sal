(n, k) = map(int, input().split())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
mod = 1000000007
ans = 1
for x in range(0, n // k):
    po = 10 ** (k - 1)
    p = c[x] * po
    q = (c[x] + 1) * po
    res = 0
    if p % b[x] == 0:
        res -= 1
    if q % b[x] == 0:
        res += 1
    if po * 10 % b[x] == 0:
        res -= 1
    res += 1
    res += 10 * po // b[x] - q // b[x] + p // b[x]
    ans = ans % mod * (res % mod) % mod
print(ans)
