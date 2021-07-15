from math import gcd

MOD = 1000000007

def inv(a, b):
    if a < 0:
        a, b = -a, -b
    return (-b, a)

def solve(n, a, b):
    zero_zero = 0
    zero = 0
    inf = 0
    D = {}
    for i in range(n):
        p, q = a[i], b[i]
        if (p == 0) and (q == 0):
            zero_zero += 1
        elif p == 0:
            zero += 1
        elif q == 0:
            inf += 1
        else:
            r = gcd(p, q)
            p, q = (p // r, q // r)
            if q < 0:
                p, q = -p, -q
            k = (p, q)
            if not k in D:
                D[k] = 0
            D[k] += 1
    group = set()
    for (p, q), v in D.items():
        if not inv(p,q) in group:
            group.add((p,q))
    pow2 = [0] * (n+1)
    pow2[0] = 1
    for i in range(n):
        pow2[i+1] = (pow2[i] * 2) % MOD
    ans = 1
    for p, q in group:
        t = pow2[D[p,q]]
        if inv(p, q) in D:
            t += pow2[D[inv(p, q)]] - 1
        ans = (ans * t) % MOD
    ans *= pow2[zero] + pow2[inf] - 1
    return (ans + zero_zero - 1) % MOD

n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
print(solve(n, a, b))
