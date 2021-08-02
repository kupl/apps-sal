a = sorted(list(map(int, input().split())))
a[2] = min(a[2], (a[0] + a[1]) * 2)
print((a[0] + a[1] + a[2]) // 3)
