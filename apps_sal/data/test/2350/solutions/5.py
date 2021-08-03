t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    print((y2 - y1) * (x2 - x1) + 1)
