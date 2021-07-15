n = int(input())
a, b, c = (list(map(int, input().split())) for i in range(3))
d1, d2 = a[0], b[0]
for i in range(1, n):
    d1, d2 = max(d2 + a[i], d1 + b[i]), max(d2 + b[i], d1 + c[i])
print(d1)
