def g(n):
    k = (n - a + 1)
    return ((n + a) * k) // 2 - b * k


x, y, a, b = list(map(int, input().split()))
a = max(a, b + 1)

if x <= b:
    print(0)
else:
    if y > x - 2:
        print(g(x))
    elif y >= a - 1:
        print((x - y - 1) * (y - b + 1) + g(y + 1))
    else:
        print((x - a + 1) * (y - b + 1))

for i in range(a, x + 1):
    for j in range(b, min(i, y + 1)):
        print(i, j)
