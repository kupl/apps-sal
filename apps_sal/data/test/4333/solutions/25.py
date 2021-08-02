x1, y1, x2, y2 = map(int, input().split())

diff_x = x2 - x1
diff_y = y2 - y1

print(x2 - diff_y, y2 + diff_x, x1 - diff_y, y1 + diff_x)
