from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))

n = int(max(a)**.5)
mark = [True] * (n + 1)
primes = []
for i in range(2, n + 1):
    if mark[i]:
        primes.append(i)
        for j in range(i, n + 1, i): mark[j] = False

d = defaultdict(int)

ans = 0
for i in a:
    t, t1 = [], []
    for j in primes:
        if i % j == 0:
            x = 0
            while i % j == 0:
                i //= j
                x += 1
            z = x % k
            if z:
                t.append((j, z))
                t1.append((j, k - z))
        elif i == 1: break
    if i != 1:
        t.append((i, 1))
        t1.append((i, k - 1))

    t = tuple(t)
    t1 = tuple(t1)

    ans += d[t1]
    d[t] += 1
print(ans)
