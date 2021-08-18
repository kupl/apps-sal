n = int(input())
d = {}
for _ in range(n):
    c = input()[0]
    d[c] = d.get(c, 0) + 1
res = 0
for v in d.values():
    x = (v + 1) // 2
    res += (x * (x - 1)) // 2
    y = v - x
    res += (y * (y - 1)) // 2
print(res)
