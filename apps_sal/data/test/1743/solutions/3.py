n = int(input())
a, b, c = (list(map(int, input().split())) for i in range(3))
u, v = a[0], b[0]
for i in range(1, n):
    u, v = max(v + a[i], u + b[i]), max(v + b[i], u + c[i])
print(u)
