import math
n = int(input())

div = [0] * 101

for i in range(2, n + 1):
    j = 2
    t = i
    while i > 1 and j <= t:
        if i % j == 0:
            div[j] += 1
            i //= j
        if i % j != 0:
            j += 1

n2 = 0
n4 = 0
n14 = 0
n24 = 0
n74 = 0

for i in range(n):
    if div[i] >= 2:
        n2 += 1
    if div[i] >= 4:
        n4 += 1
    if div[i] >= 14:
        n14 += 1
    if div[i] >= 24:
        n24 += 1
    if div[i] >= 74:
        n74 += 1

print((n24 * (n2 - 1) + n14 * (n4 - 1) + n4 * (n4 - 1) // 2 * (n2 - 2) + n74))
