# ARC109 A

a, b, x, y = list(map(int, input().split()))

ans, c, d = 0, 0, 0

if a == b:
    ans = x
elif a > b:
    c = x + (a - b - 1) * y
    d = (a - b) * 2 * x - x
    ans = min(c, d)
else:
    c = (b - a) * 2 * x + x
    d = (b - a) * y + x
    ans = min(c, d)

print(ans)
