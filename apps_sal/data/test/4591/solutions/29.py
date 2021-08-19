#n = int(input())
a, b, c, x, y = list(map(int, input().split()))
#al = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]
mn = a * x + b * y
for i in range(0, max(x, y) + 1):
    mn = min(mn, max(x - i, 0) * a + max(y - i, 0) * b + 2 * i * c)
print(mn)
