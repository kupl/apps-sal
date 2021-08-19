(n, x) = map(int, input().split())
a = list(map(int, input().split()))
count = 0
for i in range(n - 1):
    if a[i] + a[i + 1] > x:
        y = a[i] + a[i + 1] - x
        count += y
        a[i + 1] = max(0, a[i + 1] - y)
print(count)
