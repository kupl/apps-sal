(n, z, w) = map(int, input().split())
a = list(map(int, input().split()))
if n == 1:
    print(abs(a[0] - w))
else:
    print(max(abs(a[n - 2] - a[n - 1]), abs(w - a[n - 1])))
