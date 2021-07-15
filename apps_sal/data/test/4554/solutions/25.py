W, a, b = map(int, input().split())

if abs(b - a) - W <= 0:
    print(0)
else:
    print(abs(b - a) - W)
