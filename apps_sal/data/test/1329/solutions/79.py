from collections import Counter


def prime_factorize(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors.append(i)
        i += 1
    if n > 1:
        factors.append(n)
    return Counter(factors)


n = int(input())

c = Counter([])
for i in range(1, n + 1):
    c += prime_factorize(i)

"""
75 = 3 * 5 * 5
75数 = {p,q,r|p,q,rは互いに素}として
 p^2 * q^4 * r^4
 p^2 * q^24
 p^4 * q^14
 p^74
"""
ans = 0
s = set([i for i, cnt in c.items() if cnt >= 4])
t = set([i for i, cnt in c.items() if cnt >= 2])
ls = len(s)
lt = len(t)
if ls >= 2:
    ans += ls * (ls - 1) // 2 * (lt - 2)

s = set([i for i, cnt in c.items() if cnt >= 24])
t = set([i for i, cnt in c.items() if cnt >= 2])
ls = len(s)
lt = len(t)
if ls >= 1:
    ans += ls * (lt - 1)

s = set([i for i, cnt in c.items() if cnt >= 14])
t = set([i for i, cnt in c.items() if cnt >= 4])
ls = len(s)
lt = len(t)
if ls >= 1:
    ans += ls * (lt - 1)

s = set([i for i, cnt in c.items() if cnt >= 74])
ls = len(s)
ans += ls

print(ans)
