(a, b, c, n) = list(map(int, input().split()))
x = n - (a + b - c)
a -= c
b -= c
if x <= 0 or a < 0 or b < 0:
    print(-1)
else:
    print(x)
