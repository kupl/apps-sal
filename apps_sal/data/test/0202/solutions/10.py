3
(x1, y1) = input().split()
(x1, y1) = (int(x1), int(y1))
(x2, y2) = input().split()
(x2, y2) = (int(x2), int(y2))
print(max(abs(x1 - x2), abs(y1 - y2)))
