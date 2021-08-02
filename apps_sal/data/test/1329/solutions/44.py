from collections import defaultdict

n = int(input())
d = defaultdict(int)


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


for i in range(1, n + 1):
    for x in prime_factorize(i):
        d[x] += 1

# print(d)


e = defaultdict(int)

l = [2, 4, 14, 24, 74]

# 74
for k, v in d.items():
    for x in l:
        if v >= x:
            e[x] += 1

# print(e)

ans = 0

ans += e[74]
ans += e[24] * (e[2] - 1)
ans += e[14] * (e[4] - 1)
ans += (e[4] * (e[4] - 1) // 2) * (e[2] - e[4]) + (e[4] * (e[4] - 1) * (e[4] - 2) // 2)

print(ans)
