read = lambda: list(map(int, input().split()))
x1, y1 = read()
x2, y2 = read()
print(max(abs(y1 - y2), abs(x1 - x2)))

