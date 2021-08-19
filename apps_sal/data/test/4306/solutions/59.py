(a, b, c, d) = map(int, input().split())
x = max(a, c)
y = min(b, d)
if 0 < y - x:
    print(y - x)
else:
    print(0)
