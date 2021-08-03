def I(): return map(int, input().split())


n, p = I()
a = list(I())
b = list(I())
r = a[p - 1] + b[0]
s = 0
for i in range(p - 1):
    if r >= b[-1] + a[i]:
        s += 1
        del b[-1]
print(p - s)
