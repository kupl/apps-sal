mod = 1000000007


def pow(a, b, c):
    n = 1
    m = a
    v = b
    if a == 1:
        return 1
    while v > 0:
        if v % 2 == 1:
            n *= m % c
            n %= c
        m *= m
        m %= c
        v //= 2
    return n % c


(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
z = [0 for i in range(n + 10)]
for i in range(n)[::-1]:
    z[i] = z[i + 1]
    if a[i] == 0:
        z[i] += 1
    if b[i] == 0:
        z[i] += 1
ans = 0
cmb = 1
if z[0] == 0:
    if a > b:
        print(1)
    else:
        print(0)
    quit()
inverse_two = pow(2, mod - 2, mod)
com = m * (m - 1) % mod * inverse_two % mod
for i in range(n):
    if a[i] != 0 and b[i] != 0:
        if a[i] > b[i]:
            ans += cmb * pow(m, z[i + 1], mod) % mod
        break
    elif a[i] == 0 and b[i] == 0:
        ans += cmb * com % mod * pow(m, z[i + 1], mod) % mod
        cmb *= m
        cmb %= mod
    elif a[i] == 0:
        ans += cmb * (m - b[i]) % mod * pow(m, z[i + 1], mod) % mod
    elif b[i] == 0:
        ans += cmb * (a[i] - 1) % mod * pow(m, z[i + 1], mod) % mod
    ans %= mod
k = pow(m, z[0], mod)
k = pow(k, mod - 2, mod)
ans *= k
ans %= mod
print(ans)
