a, b, x, y = list(map(int, input().split()))
vertical = min(2 * x, y)
d = abs(a - b)
if a > b:
    ans = (d - 1) * vertical + x
else:
    ans = d * vertical + x
print(ans)
