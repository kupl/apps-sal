a, b, c, d = map(int, input().split())
e = 0
f = 0
if a < c:
    e = c
else:
    e = a
if b < d:
    f = b
else:
    f = d
if e <= f:
    print(f - e)
else:
    print(0)
