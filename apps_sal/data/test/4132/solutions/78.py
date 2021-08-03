n = int(input())
a = list(map(int, input().split()))

x = a[0]
for i in range(1, n):
    x, y = max(x, a[i]), min(x, a[i])
    while y != 0:
        x, y = y, x % y
print(x)
