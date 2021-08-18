from collections import Counter


def f(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = int(input())
if n == 1:
    print(1)
    return
d = {}
mod = 10**9 + 7
d[2] = 1
for i in range(3, n + 1):
    x = f(i)
    c = Counter(x)
    for j in c.keys():
        if j not in d:
            d[j] = c[j]
        else:
            d[j] += c[j]
        d[j] = d[j] % mod
ans = 1
for i in d.keys():
    ans *= d[i] + 1
print(ans % mod)
