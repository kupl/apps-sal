a, b, c, x, y = list(map(int, input().split()))
if x < y:
    a, b, x, y = b, a, y, x

if a + b < 2 * c:
    ans = a * x + b * y
else:
    if a > 2 * c:
        ans = c * 2 * x
    else:
        ans = c * 2 * y + a * (x - y)
print(ans)
