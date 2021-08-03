x, y = map(int, input().split())
print(max(x + y, x + (x - 1), y + (y - 1)))
