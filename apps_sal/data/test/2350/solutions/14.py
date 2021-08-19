t = int(input())
for i in range(t):
    (x1, x2, y1, y2) = map(int, input().split())
    print(1 + abs(y1 - x1) * abs(y2 - x2))
