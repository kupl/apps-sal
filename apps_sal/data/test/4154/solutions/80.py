n, m = list(map(int, input().split()))
a = [] * m
b = [] * m
for i in range(m):
    l, r = list(map(int, input().split()))
    a.append(l)
    b.append(r)

if max(a) <= min(b):
    print((min(b) - max(a) + 1))
else:
    print((0))
