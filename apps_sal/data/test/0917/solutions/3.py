n, h, m = map(int, input().split())
k = [h] * (n + 1)
for _ in range(m):
    l, r, x = map(int, input().split())
    for i in range(l, r + 1):
        k[i] = min(k[i], x)
t = 0
for i in range(1, n + 1):
    t += k[i]**2
print(t)
