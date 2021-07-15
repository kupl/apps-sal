x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))

print(2 * (max(2, abs(x1 - x2) + 1) + max(2, abs(y1 - y2) + 1)))
