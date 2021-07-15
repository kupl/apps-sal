from math import sqrt
n, m, k = list(map(int, input().split()))

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

ac = [0] * (n + 1)
bc = [0] * (m + 1)

cs = 0

for ai in a:
    if ai == 1:
        cs += 1
    if ai == 0:
        ac[cs] += 1
        cs = 0
ac[cs] += 1

cs = 0
for bi in b:
    if bi == 1:
        cs += 1
    if bi == 0:
        bc[cs] += 1
        cs = 0
bc[cs] += 1

pairs = []

for i in range(1, int(sqrt(k) + 1)):
    if k % i == 0:
        pairs.append((i, k // i))

total = 0

for i, j in pairs:
    if i <= n and j <= m:
        act = 0
        for k in range(i, n + 1):
            act += ac[k] * (k - i + 1)
        bct = 0
        for k in range(j, m + 1):
            bct += bc[k] * (k - j + 1)

        total += act * bct
    if j <= n and i <= m and i != j:
        act = 0
        for k in range(j, n + 1):
            act += ac[k] * (k - j + 1)
        bct = 0
        for k in range(i, m + 1):
            bct += bc[k] * (k - i + 1)

        total += act * bct

print(total)

