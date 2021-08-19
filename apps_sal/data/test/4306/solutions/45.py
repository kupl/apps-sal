(a, b, c, d) = map(int, input().split())
e = min(b, d) - max(a, c)
if e >= 0:
    print(e)
else:
    print(0)
