(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a, reverse=True)
b = sorted(b, reverse=True)
res = max(a[0] * b[0], a[-1] * b[-1], a[0] * b[-1], a[-1] * b[0])
if res == a[0] * b[0] or res == a[0] * b[-1]:
    a.remove(a[0])
else:
    a.remove(a[-1])
res = max(a[0] * b[0], a[-1] * b[-1], a[0] * b[-1], a[-1] * b[0])
print(res)
