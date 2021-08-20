(K, N) = map(int, input().split())
P = 998244353
fa = [1]
for i in range(1, 10000):
    fa.append(fa[-1] * i % P)
fainv = [pow(fa[-1], P - 2, P)]
for i in range(1, 10000)[::-1]:
    fainv.append(fainv[-1] * i % P)
fainv = fainv[::-1]


def C(a, b):
    if not (a >= 0 and 0 <= b <= a):
        return 0
    return fa[a] * fainv[a - b] * fainv[b] % P


A = []
for i in range(1, (K + 1) // 2 + 1):
    s = 0
    for j in range(i + 1):
        s += C(N + K - 1 - 2 * j, K - 1) * C(i, j) * (-1) ** j
        s %= P
    A.append(s)
for i in range(2 * K - 1):
    print(A[min(i // 2, (2 * K - i - 2) // 2)])
