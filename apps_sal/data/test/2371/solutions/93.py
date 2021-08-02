n, z, w = list(map(int, input().split()))
a = list(map(int, input().split()))
if n == 1:
    print((abs(a[0] - w)))
    return
print((max(abs(a[-1] - w), abs(a[-1] - a[-2]))))
