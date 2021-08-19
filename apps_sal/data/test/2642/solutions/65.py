import math
N = int(input())
MOD = 10 ** 9 + 7
fish = {}
ans = 1
a = 0
b = 0
w = 0
for i in range(N):
    (A, B) = map(int, input().split())
    if A == 0 and B == 0:
        w += 1
    elif A == 0:
        a += 1
    elif B == 0:
        b += 1
    else:
        c = math.gcd(A, B)
        A = A // c
        B = B // c
        if B < 0:
            (A, B) = (-A, -B)
        k = (A, B)
        if not k in fish:
            fish[k] = 0
        fish[k] += 1
group = set()
for ((p, q), v) in fish.items():
    (invp, invq) = (-q, p)
    if invq < 0:
        (invp, invq) = (-invp, -invq)
    if not (invp, invq) in group:
        group.add((p, q))
for (p, q) in group:
    (invp, invq) = (-q, p)
    if invq < 0:
        (invp, invq) = (-invp, -invq)
    t = 2 ** fish[p, q]
    if (invp, invq) in fish:
        t += 2 ** fish[invp, invq] - 1
    ans = ans * t % MOD
ans *= 2 ** a + 2 ** b - 1
ans = ans + w - 1
print(ans % MOD)
