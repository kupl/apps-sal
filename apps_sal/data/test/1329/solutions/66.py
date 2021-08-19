from collections import defaultdict
import math
n = int(input())


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


d = defaultdict(int)

p = []
for i in range(2, n + 1):
    if is_prime(i):
        d[i] = 1
        p.append(i)
        continue
    x = i
    for j in p:
        while x % j == 0:
            x //= j
            d[j] += 1

# 75
c = 0
for i in list(d.values()):
    if i >= 74:
        c += 1
ans = c

#25 * 3
c, e = 0, 0
for i in list(d.values()):
    if i >= 24:
        c += 1
    if i >= 2:
        e += 1
ans += c * (e - 1)

#15 * 5
c, e = 0, 0
for i in list(d.values()):
    if i >= 14:
        c += 1
    if i >= 4:
        e += 1
ans += c * (e - 1)

#5 * 5 * 3
c, e = 0, 0
for i in list(d.values()):
    if i >= 4:
        c += 1
    if i >= 2:
        e += 1
ans += (c * (c - 1) // 2) * (e - 2)

print(ans)
