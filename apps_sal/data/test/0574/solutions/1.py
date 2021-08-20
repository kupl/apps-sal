(x1, y1, x2, y2) = list(map(int, input().split(' ')))
b = int((y2 - y1 + 1) / 2) + 1
s = b - 1
l = x2 - x1 + 1
ans = b * int((l + 1) / 2) + s * int(l / 2)
print(ans)
