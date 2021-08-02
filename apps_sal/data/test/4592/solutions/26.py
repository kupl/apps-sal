n = int(input())
d = {}
for x in range(2, n + 1):
    while x % 2 < 1:
        x //= 2
        d[2] = d.get(2, 0) + 1
    for i in range(3, int(x**0.5) + 1, 2):
        while x % i < 1:
            x //= i
            d[i] = d.get(i, 0) + 1
        if x < 2: break
    if x > 1: d[x] = d.get(x, 0) + 1
a = 1
for v in d.values(): a = a * (v + 1) % (10**9 + 7)
print(a)
