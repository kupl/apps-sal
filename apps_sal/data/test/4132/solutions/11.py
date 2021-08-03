n = int(input())
a = list(map(int, input().split()))

x = a[0]
for i in range(1, n):
    y = a[i]
    x, y = max(x, y), min(x, y)
    while y != 0:
        x, y = y, x % y
print(x)
