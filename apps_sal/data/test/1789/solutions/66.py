a, b, x, y = map(int, input().split())
v = min(y, 2 * x)

if a == b:
    print(x)
    return

v = min(2 * x, y)
if a > b:
    ans = v * (a - b - 1) + x
else:
    ans = v * (b - a) + x
print(ans)
