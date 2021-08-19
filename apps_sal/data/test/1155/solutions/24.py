(n, m) = map(int, input().split())
a = []
for i in range(n):
    (x, y) = map(int, input().split())
    a.append(x / y * m)
print(min(a))
