n, m = [int(x)for x in input().split()]
ns = input()
ms = input()
if n > m:
    n = m
    ns = ns[-m:]

mod = 998244353
sq2 = [2]

for i in range(32):
    x = sq2[-1] * sq2[-1] % mod
    sq2.append(x)

p1 = [1]
for i in range(n + 1):
    p1.append(p1[-1] * 2 % mod)


def pow2(n):
    ans = 1
    for i in range(32):
        if (n >> i) & 1 == 1:
            ans *= sq2[i]
            ans %= mod
    return ans


z = []
sum = 0
for i in range(m):
    if ms[i] == '0':
        sum += 1
    z.append(sum)

ans = 0
for i in range(n):
    if ns[i] == '0':
        continue
    q = n - i - 1

    l = i - (n - m)

    ti = 0
    if l >= 0:
        zn = z[l]
        ti = l - zn + 1
    else:
        ti = l
    ans += ti * p1[q]
    ans %= mod

print(ans % mod)
