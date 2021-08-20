(n, d) = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = 0
for i in range(n):
    for j in range(i + 1, n):
        s = 0
        for (c, e) in zip(a[i], a[j]):
            s += (c - e) ** 2
        if s ** 0.5 == int(s ** 0.5):
            b += 1
print(b)
