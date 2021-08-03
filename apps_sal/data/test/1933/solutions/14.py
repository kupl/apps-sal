n, m, k = map(int, input().split())
x, y = 0, 0
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in zip(*a):
    u, v = 0, 0
    for j in range(n - k + 1):
        p, q = sum(i[j:j + k]), sum(i[:j])
        if p > u:
            u = p
            v = q
    x += u
    y += v

print(x, y)
