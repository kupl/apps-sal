n, k = map(int, input().split())
mod = 10**9 + 7
count = [0] * (k + 1)


def getnum(m):
    ret = pow(k // m, n, mod)
    mul = 2
    while m * mul <= k:
        ret -= count[m * mul]
        mul += 1
    return ret % mod


ans = 0
for i in range(1, k + 1)[::-1]:
    g = getnum(i)
    count[i] = g
    ans += g * i
    ans %= mod
print(ans)
