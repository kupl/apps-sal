p, q = [int(x) for x in input().split()]
n = int(input())
a = [int(x) for x in input().split()]

x, y, i = 1, 0, n
while n > 0:
    x, y = y, x
    n -= 1
    x += y * a[n]

if x * q == y * p:
    print("YES")
else:
    print("NO")
