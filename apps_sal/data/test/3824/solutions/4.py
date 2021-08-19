(x1, y1) = map(int, input().split())
(x2, y2) = map(int, input().split())
print(2 * (max(abs(x1 - x2) + 1, 2) + max(abs(y1 - y2) + 1, 2)))
