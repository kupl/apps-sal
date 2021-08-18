MOD = 10**9 + 7


def fast_pow(x, n, MOD):
    res = 1
    while n:
        if n & 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>= 1
    return res


n = int(input())
a = list(map(int, input().split()))

d = {}
for i in a:
    if n % 2:
        if i > 0 and i % 2:
            print((0))
            return
    else:
        if i > 0 and i % 2 == 0:
            print((0))
            return

    if not i in d:
        d[i] = 1
    elif d[i] == 1:
        d[i] += 1
    else:
        print((0))
        return

if n % 2:
    if d[0] != 1:
        print((0))
        return
    print((fast_pow(2, len(d) - 1, MOD)))
else:
    if 0 in d:
        print((0))
        return
    print((fast_pow(2, len(d), MOD)))
