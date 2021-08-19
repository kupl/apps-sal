(x, y, x1, y1) = list(map(int, input().split()))
res1 = (y1 - y + 1) // 2
res2 = y1 - y + 1 - res1
resx1 = (x1 - x + 1) // 2
resx2 = x1 - x + 1 - resx1
print(res1 * resx1 + res2 * resx2)
