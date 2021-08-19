(a, b, x, y) = map(int, input().split())
if a > b:
    tmp = x + (a - b - 1) * y
    tmp2 = (a - b) * x + (a - b - 1) * x
    print(min(tmp, tmp2))
elif a == b:
    print(x)
else:
    tmp = x + (b - a) * y
    tmp2 = (b - a) * x + (b - a + 1) * x
    print(min(tmp, tmp2))
