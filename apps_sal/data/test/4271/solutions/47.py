n = int(input())
(a, b, c) = [list(map(int, input().split())) for i in range(3)]
x = 0
d = -10
for i in range(n):
    y = b[a[i] - 1]
    x += y
    if a[i] - 1 == d:
        x += c[d - 1]
    d = a[i]
print(x)
