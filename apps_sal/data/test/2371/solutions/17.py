n, z, w, *a = list(map(int, open(0).read().split()))
if n > 1:
    print((max(abs(a[-2] - a[-1]), abs(a[-1] - w))))
else:
    print((abs(a[0] - w)))
