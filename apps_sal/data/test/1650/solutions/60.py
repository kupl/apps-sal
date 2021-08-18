def pow_mod(x, y, mod=10**9 + 7):
    if y == 0:
        return 1
    res = 1
    for i in range(y.bit_length()):
        if y & (1 << i):
            res *= x
            res %= mod
        x *= x
        x %= mod
    return res


def calc(r):
    if r <= 1:
        return 3
    return pow_mod(3, r - 1) * 2


l = input()
n = len(l)
mod = 10**9 + 7

count = [0] * (n + 1)
for i in range(1, n + 1):
    count[i] = calc(i) + count[i - 1]

ans = 0
cnt = 0
u = n
for i in range(n):
    u -= 1
    if i == n - 1:
        if l[i] == "1":
            ans += 3 * pow_mod(2, cnt) % mod
            ans %= mod
        else:
            ans += pow_mod(2, cnt) % mod
            ans %= mod
        continue
    if l[i] == "1":
        ans += count[u] % mod * pow_mod(2, cnt) % mod
        ans %= mod
        cnt += 1
        pass
    else:
        pass

print((ans % mod))
