n, c = map(int, input().split())
a = list(map(int, input().split()))
m = 0
for i in range(n - 1):
    if a[i] - a[i + 1] - c > m:
        m = a[i] - a[i + 1] - c
print(m)
