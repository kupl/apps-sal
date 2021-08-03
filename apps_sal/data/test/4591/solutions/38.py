a, b, c, x, y = list(map(int, input().split()))

ans = [a * x + b * y]

if x >= y:
    ans.append(2 * c * y + (x - y) * a)
    ans.append(2 * c * x)
else:
    ans.append(2 * c * x + (y - x) * b)
    ans.append(2 * c * y)

print((min(ans)))
