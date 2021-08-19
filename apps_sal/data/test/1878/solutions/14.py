n = int(input())
total = 0
for i in range(n):
    (x1, y1, x2, y2) = map(int, input().split())
    total += (x2 - x1 + 1) * (y2 - y1 + 1)
print(total)
