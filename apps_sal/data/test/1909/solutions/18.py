n, k = map(int, input().split())
a = list(map(int, input().split())) * 2
for i in range(n + n - k - 1, -1, -1):
    a[i] += a[i + k]
mi, mm = 0, float("inf")
for i in range(n):
    x = a[i] - a[i + n]
    if mm > x:
        mi = i
        mm = x
print(mi + 1)
