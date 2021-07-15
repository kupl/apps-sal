tests = int(input())
for _ in range(tests):
    x1, y1, x2, y2 = map(int, input().split())
    print((x2 - x1) * (y2 - y1) + 1)
