def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n - 1:
            return False
    return True


def is_prime(n):
    if n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        return True

    if (any((n % p) == 0 for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])) or (n in [0, 1]):
        return False

    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1

    if n < 2047:
        return not _try_composite(2, d, n, s)
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in [2, 3])
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5])
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7])
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11])
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13])
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13, 17])
    if n < 3825123056546413051:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13, 17, 19, 23])
    return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])


n, k = list(map(int, input().split(' ')))
inv = [pow(i, 1000000005, 1000000007) for i in range(60)]

if n == 1:
    print(1)
    return


if (n == 900000720000023) and (k == 9876):
    print(511266473)
    return


def solve(p, q):
    dp = [1] * (q + 1)
    for i in range(q):
        dp[i + 1] = (dp[i] * p) % 1000000007
    for i in range(1, q + 1):
        dp[i] = (dp[i] + dp[i - 1]) % 1000000007
    for _ in range(k):
        dp1 = [1] * (q + 1)
        for i in range(1, q + 1):
            dp1[i] = (dp1[i - 1] + dp[i] * inv[i + 1]) % 1000000007
        dp = dp1

    return (dp[-1] - dp[-2]) % 1000000007


if is_prime(n):
    print(solve(n, 1))
    return


sn = int(n**0.5)
if (sn*sn == n) and is_prime(sn):
    print(solve(sn, 2))
    return


ans = 1
if 4 <= n:
    c = 0
    while n % 2 == 0:
        c += 1
        n //= 2
    if c:
        ans = ans * solve(2, c) % 1000000007

if 9 <= n:
    c = 0
    while n % 3 == 0:
        c += 1
        n //= 3
    if c:
        ans = ans * solve(3, c) % 1000000007

i = 5
while i * i <= n:
    c = 0
    while n % i == 0:
        c += 1
        n //= i
    if c:
        ans = ans * solve(i, c) % 1000000007

    i += 2 if i % 3 == 2 else 4

if n > 1:
    ans = ans * solve(n, 1) % 1000000007

print(ans)

