from collections import Counter


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = int(input())

l = prime_factorize(n)
c = Counter(l)
v = c.values()
ans = 0
for i in v:
    a = 0
    for j in range(1, 1000000):
        a += j
        if a > i:
            ans += j - 1
            break
print(ans)
