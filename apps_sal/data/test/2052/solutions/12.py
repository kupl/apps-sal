w, l = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
s = res = sum(a[:l])
for i in range(l, w - 1):
    s += a[i] - a[i - l]
    res = min(res, s)
print(res)

