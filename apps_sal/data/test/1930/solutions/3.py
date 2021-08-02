K = 998244353


def mu(a, n):
    if n == 0: return 1
    q = mu(a, n // 2)
    if n % 2 == 0: return q * q % K
    return q * q % K * a % K


MAXN = 200005
dd = [0 for i in range(MAXN)]
p = [0 for i in range(MAXN)]
s = [0 for i in range(MAXN)]
a = [0 for i in range(MAXN)]
fen = [0 for i in range(MAXN)]


def add(u, v):
    i = u
    while (i <= 200000):
        fen[i] += v
        i += i & -i


def get(u):
    res = 0
    i = u
    while (i > 0):
        res += fen[i]
        i -= i & -i
    return res


n = int(input())

data = input().split()

cnt = 0

for i in range(1, n + 1):
    p[i] = int(data[i - 1])
    if (p[i] > 0): dd[p[i]] = 1
    else: cnt += 1

for i in range(1, n + 1):
    if (dd[i] == 0):
        s[i] = s[i - 1] + 1
    else:
        s[i] = s[i - 1]

cnt1 = 0
P = 0
den = mu(cnt, K - 2)
for i in range(1, n + 1):
    if (p[i] == -1):
        cnt1 += 1
    else:
        u = cnt - cnt1
        P = (P + u * s[p[i]] % K * den % K) % K
        P = (P + cnt1 * (cnt - s[p[i]]) % K * den % K) % K

P = (P + cnt * (cnt - 1) * mu(4, K - 2)) % K

m = 0

for i in range(1, n + 1):
    if p[i] > 0:
        m += 1
        a[m] = p[i]

P1 = 0
for i in range(m, 0, -1):
    P1 = (P1 + get(a[i])) % K
    add(a[i], 1)

P = (P + P1) % K

print(P)
