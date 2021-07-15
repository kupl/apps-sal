MOD = 1000000007
OBRAT = [-1] * 2000
CC = {}
FACT = [-1] * 2000
OBRAT_FACT = [-1] * 2000


def obrat(k):
    if OBRAT[k] == -1:
        OBRAT[k] = fast_pow(k, MOD - 2)
    return OBRAT[k]


def c(n, k):
    if (n, k) in CC:
        return CC[(n, k)]
    res = fact(n)
    res = (res * obrat_fact(k)) % MOD
    res = (res * obrat_fact(n - k)) % MOD
    CC[(n, k)] = res
    return res


def obrat_fact(k):
    if OBRAT_FACT[k] != -1:
        return OBRAT_FACT[k]
    res = 1
    for i in range(2, k + 1):
        res = (res * obrat(i)) % MOD
    OBRAT_FACT[k] = res
    return res


def fact(n):
    if FACT[n] != -1:
        return FACT[n]
    res = 1
    for i in range(2, n + 1):
        res = (res * i) % MOD
    FACT[n] = res
    return res


def fast_pow(x, y):
    if y == 0:
        return 1
    p = fast_pow(x, y // 2) % MOD
    p = p * p % MOD
    if y % 2:
        p = p * x % MOD
    return p


s = input()
k = int(input())
n = len(s)

if k == 1:
    print(n - 1)
    return
if k == 0:
    print(1)
    return

moves = [0] * 1025
moves[1] = 0
for i in range(2, 1024):
    ii = i
    ones = 0
    while ii > 0:
        if ii % 2 == 1:
            ones += 1
        ii //= 2
    moves[i] = moves[ones] + 1

if n < 10:
    d = 1
    a = 0
    for i in range(n - 1, -1, -1):
        a += d * int(s[i])
        d *= 2
    res = 0
    for i in range(2, a + 1):
        if moves[i] == k:
            res += 1
    print(res)
    return

res = 0
if moves[s.count('1')] == k - 1:
    res += 1
for i in range(1, 1024):
    ki = moves[i]
    if ki != k - 1:
        continue
    m = n - 1
    j = 0
    while m >= i and i >= 0 and m >= 0:
        res = (res + c(m, i)) % MOD
        i -= 1
        j += 1
        while j < n and s[j] != '1':
            j += 1
        m = n - 1 - j

print(res)

