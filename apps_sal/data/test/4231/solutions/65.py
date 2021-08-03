h, w = map(int, input().split())
x, y = map(int, input().split())
print(h * w - w * x - h * y + x * y)
