(n, z, w) = map(int, input().split())
a = list(map(int, input().split()))
if n == 1:
    print(abs(a[0] - w))
else:
    print(max(abs(a[-1] - a[-2]), abs(a[-1] - w)))
