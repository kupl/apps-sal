(x1, y1, x2, y2) = map(int, input().split())
d = (x2 - x1) // 2 + 1
e = (y2 - y1) // 2 + 1
if (y2 - y1) % 2 == 0:
    ans = d * e + (d - 1) * (e - 1)
else:
    ans = (2 * d - 1) * (e - 1)
print(ans)
