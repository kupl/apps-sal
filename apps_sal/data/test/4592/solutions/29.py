n = int(input())
mod = 10**9 + 7


def factors(N):
    factors = []
    while N % 2 == 0:
        factors.append(2)
        N //= 2

    for f in range(3, int(N**0.5) + 1, 2):
        while N % f == 0:
            factors.append(f)
            N //= f
    if N != 1:
        factors.append(N)
    return factors


cd = dict()
for i in range(1, n + 1):
    facs = factors(i)
    for f in facs:
        cd.setdefault(f, 0)
        cd[f] += 1

ans = 1
for key, v in list(cd.items()):
    ans *= (v + 1)
    ans %= mod

print(ans)
