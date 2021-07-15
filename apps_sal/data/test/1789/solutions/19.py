a, b, x, y = map(int, input().split())
if b - a > 0:
    d = b - a
    print(min(x+d*y, d*2*x+x))
elif b - a < 0:
    d = a - b
    print(min((d-1)*y+x, d*2*x-x))
else:
    print(x)
