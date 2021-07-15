a, b, c, d = map(int, input().split())
if a > c: a, b, c, d = c, d, a, b
if b < c: print(0)
elif b < d: print(b - c)
else: print(d - c)
