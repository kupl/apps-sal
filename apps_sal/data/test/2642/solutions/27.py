from collections import defaultdict
(n, *L) = list(map(int, open(0).read().split()))
mod = 10 ** 9 + 7
d = defaultdict(lambda: [0, 0])


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


two = [1] * (n + 1)
for i in range(n):
    two[i + 1] = two[i] * 2 % mod
zero = 0
for (a, b) in zip(*[iter(L)] * 2):
    if a == b == 0:
        zero += 1
        continue
    if a == 0:
        d[0, 1][0] += 1
    elif b == 0:
        d[0, 1][1] += 1
    else:
        g = gcd(a, b)
        a //= g
        b //= g
        if a * b > 0:
            d[a, b][0] += 1
        else:
            d[abs(b), abs(a)][1] += 1
ans = 1
for ((_, _), (x, y)) in list(d.items()):
    ans *= (two[x] + two[y] - 1) % mod
    ans %= mod
print((ans + zero + mod - 1) % mod)
