n = int(input())
a = list(map(int, input().split(' ')))
a = sorted(a)
x = 0
y = 0
for i in range(n // 2):
    y += a[i]
for i in range(n // 2, n):
    x += a[i]
res = x * x + y * y
print(res)
