n, k = list(map(int, input().split()))
a = sorted(map(int, input().split()))
d = [a[i + 1] - a[i] for i in range(n - 1)]

mod = 1000000007
def pow(x, n):
    ret = 1
    while n > 0:
        if (n & 1) == 1:
            ret = (ret * x) % mod
        x = (x * x) % mod
        n //= 2
    return ret

fac = [1]
inv = [1]
for i in range(1, n + 1):
    fac.append((fac[-1] * i) % mod)
    inv.append(pow(fac[i], mod - 2))

def cmb(n, k):
    if k < 0 or k > n:
        return 0
    return ((fac[n] * inv[k]) % mod * inv[n - k]) % mod

ret = 0
for i in range(n - 1):
    num = (cmb(n, k) - cmb(i + 1, k) - cmb(n - i - 1, k)) % mod
    ret = (ret + d[i] * num) % mod
print(ret)

