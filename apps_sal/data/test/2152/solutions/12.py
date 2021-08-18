import sys


n = int(input())
a = []
p = []
for i in range(n):
    x, y = [int(i) for i in input().split()]
    a.append(x)
    p.append(y)

ans, price = 0, p[0]
for i in range(n):
    price = min(price, p[i])
    ans += a[i] * price

print(ans)
