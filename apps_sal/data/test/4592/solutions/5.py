from collections import defaultdict
d = defaultdict(int)


def prime_factorize(n):
    while n % 2 == 0:
        d[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            d[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        d[n] += 1
    return


N = int(input())
MOD = int(1000000000.0) + 7
ans = 1
for i in range(1, N + 1):
    prime_factorize(i)
for v in d.values():
    ans = ans * (v + 1) % MOD
print(ans)
