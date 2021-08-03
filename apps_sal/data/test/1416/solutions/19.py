n, w = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
b = a[n]
g = a[0]
if b >= 2 * g:
    ret = g * 2 * n + g * n
elif b >= g:
    ret = b * n + float(b) / 2 * n
print(min(ret, w))
