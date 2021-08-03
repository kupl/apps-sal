def solve1(a, l, r, k, mod):
    n = len(a)

    if l == 0 and r == n:
        return k * (k - 1) ** (n - 1)

    if l == 0 or r == n:
        return (k - 1) ** (r - l)

    x = a[l - 1]
    y = a[r]

    dp0 = [0] * (r - l)
    dp1 = [0] * (r - l)

    if x != y:
        dp0[0] = k - 2
        dp1[0] = 1
    else:
        dp0[0] = k - 1
        dp1[0] = 0

    for i in range(1, (r - l)):
        dp0[i] = dp0[i - 1] * (k - 2) + dp1[i - 1] * (k - 1)
        dp1[i] = dp0[i - 1]

        dp0[i] %= mod
        dp1[i] %= mod

    return dp0[-1]


def solve(a, k, mod):
    n = len(a)

    res = 1

    i = 0
    while i < n:
        if i < n - 1 and a[i] != -1 and a[i] == a[i + 1]:
            return 0

        if a[i] != -1:
            i += 1
            continue

        j = i

        while j < n and a[i] == a[j]:
            j += 1

        res *= solve1(a, i, j, k, mod)

        i = j
    return res


n, k = list(map(int, (input().split())))

src = list(map(int, (input().split())))

e = src[0::2]
o = src[1::2]

mod = 998244353

print(solve(e, k, mod) * solve(o, k, mod) % mod)
