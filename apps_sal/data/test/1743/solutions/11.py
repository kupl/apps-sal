n = int(input())
R = lambda: [int(i) for i in input().split()]
a, b, c = R(), R(), R()
x, y = a[0], b[0]
for i in range(1, n):
    x, y = max(a[i] + y, b[i] + x), max(b[i] + y, c[i] + x)
print(x)
