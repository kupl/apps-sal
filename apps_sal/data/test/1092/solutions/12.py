#from itertools import permutations
#from operator import itemgetter, attrgetter
#from functools import reduce
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
MOD = int(1e9 + 7)
f = [1]
for i in range(1, 1000):
    f.append((f[-1] * i) % MOD)


def bigmod(a, e, m):
    ret = 1
    while (e):
        if (e % 2 == 1):
            ret *= a
            if (ret > m):
                ret %= m
            e -= 1
        a *= a
        e /= 2
        if (a > m):
            a %= m
    return ret


def invmod(a, p):
    return bigmod(a, p - 2, p)


ans = f[n - m]
for i in range(1, m):
    mid = a[i] - a[i - 1] - 1
    if mid > 0:
        ans *= invmod(f[mid], MOD)
        ans %= MOD
    if (mid > 1):
        ans *= bigmod(2, mid - 1, MOD)
        ans %= MOD
if a[0] > 1:
    ans *= invmod(f[a[0] - 1], MOD)
    ans %= MOD
if a[m - 1] < n:
    ans *= invmod(f[n - a[m - 1]], MOD)
    ans %= MOD
print(ans)
