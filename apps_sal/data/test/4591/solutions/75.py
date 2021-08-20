(a, b, c, x, y) = map(int, input().split())
ans = 0
if a + b >= c * 2:
    ans = min(x, y) * c * 2
    if x > y:
        if a > c * 2:
            ans += c * 2 * (x - y)
        else:
            ans += a * (x - y)
    elif b > c * 2:
        ans += c * 2 * (y - x)
    else:
        ans += b * (y - x)
else:
    ans = a * x + b * y
print(ans)
