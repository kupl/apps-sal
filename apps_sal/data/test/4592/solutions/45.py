d = {}
for i in range(int(input()) + 1):
    for j in d:
        while i % j < 1: d[j] += 1; i //= j
    if i > 1: d[i] = 2
a = 1
for v in d.values(): a = a * v % (10**9 + 7)
print(a)
