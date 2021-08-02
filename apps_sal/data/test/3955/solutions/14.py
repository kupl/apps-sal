import math
a = list(map(int, input().split()))
n = a[0]
k = a[1]
x = a[2]
a = list(map(int, input().split()))
b = [None] * n
c = [None] * n
b[0] = a[0]
mul = 1
c[n - 1] = a[n - 1]
for i in range(k):
    mul *= x
if n == 1:
    print(mul * a[0])
else:
    for i in range(1, n):
        b[i] = b[i - 1] | a[i]
    for i in range(n - 2, -1, -1):
        c[i] = c[i + 1] | a[i]
    ans = max(a[0] * mul | c[1], a[n - 1] * mul | b[n - 2])
    for i in range(1, n - 1):
        ans = max(ans, a[i] * mul | b[i - 1] | c[i + 1])
    print(ans)
