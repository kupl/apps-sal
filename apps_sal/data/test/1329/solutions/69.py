import collections

n = int(input())

div = []

for i in range(1, n + 1):
    for j in range(2, int(n**0.5) + 1):
        while i % j == 0:
            div.append(j)
            i //= j
    if i > 1:
        div.append(i)

c = collections.Counter(div)

n2, n4, n14, n24, n74 = 0, 0, 0, 0, 0

for k, v in list(c.items()):
    if v >= 2:
        n2 += 1
    if v >= 4:
        n4 += 1
    if v >= 14:
        n14 += 1
    if v >= 24:
        n24 += 1
    if v >= 74:
        n74 += 1

ans = n74 + n24 * (n2 - 1) + n14 * (n4 - 1) + n4 * (n4 - 1) * (n2 - 2) // 2

print(ans)
