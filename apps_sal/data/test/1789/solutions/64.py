(a, b, x, y) = map(int, input().split())
if b > a:
    ans = x + (b - a) * min(2 * x, y)
elif b < a:
    ans = x + (a - b - 1) * min(2 * x, y)
else:
    ans = x
print(ans)
