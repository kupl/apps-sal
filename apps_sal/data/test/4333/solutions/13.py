x1, y1, x2, y2 = map(int, input().split())
x3, y3 = x2 - (y2 - y1), y2 + x2 - x1
x4, y4 = x1 - (y2 - y1), y1 + x2 - x1

ans = [x3, y3, x4, y4]
print(*ans)
