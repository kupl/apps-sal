(a, b, c, n) = list(map(int, input().strip().split()))
a -= c
b -= c
if a < 0 or b < 0 or a + b + c > n - 1:
    print('-1')
else:
    print(n - a - b - c)
