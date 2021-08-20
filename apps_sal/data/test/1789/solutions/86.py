(a, b, x, y) = map(int, input().split())
ans = 0
if a > b:
    a1 = x + y * (a - b - 1)
    a2 = x * (2 * (a - b) - 1)
else:
    a1 = x + y * (b - a)
    a2 = x * (2 * (b - a) + 1)
ans = min(a1, a2)
print(ans)
