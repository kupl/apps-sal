(n, z, w) = map(int, input().split())
a = list(map(int, input().split()))
if n == 1:
    print(abs(a[0] - w))
else:
    p = abs(a[-2] - a[-1])
    q = abs(a[-1] - w)
    print(max(p, q))
