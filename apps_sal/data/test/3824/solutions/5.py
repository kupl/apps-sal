x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
print(2 * max(abs(x2 - x1), 1) + 2 * max(abs(y2 - y1), 1) + 4)
