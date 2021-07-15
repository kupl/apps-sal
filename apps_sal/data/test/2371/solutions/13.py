n, z, w = map(int, input().split())
a = list(map(int, input().split()))
print(abs(a[0] - w) if n == 1 else max(abs(a[n - 1] - w), abs(a[n - 2] - a[n - 1])))
