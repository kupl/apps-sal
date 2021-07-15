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
c = Counter(prime_factorize(n))
v = list(c.values())

ans = 0
for i in v:
    k = i
    s = 0
    for j in range(1, i+1):
        s += j
        if s <= k:
            ans += 1
        else:
            break
print(ans)
