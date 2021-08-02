N, M = map(int, input().split())
mod = pow(10, 9) + 7


def comb(n, k):
    if k > n - k:
        return comb(n, n - k)
    mul, div = 1, 1
    for i in range(k):
        mul = mul * (n - i) % mod
        div = div * (k - i) % mod
    ret = mul * pow(div, mod - 2, mod) % mod
    return ret


i = 2
ans = 1
tmp = M
while i * i <= M:
    if tmp % i == 0:
        cnt = 0
        while tmp % i == 0:
            tmp //= i
            cnt += 1
        ans = ans * comb(cnt + N - 1, N - 1) % mod
    i += 1
if tmp != 1:
    ans = ans * comb(1 + N - 1, N - 1) % mod
print(ans)
