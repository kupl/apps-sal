h, w = map(int, input().split())
s, t = map(int, input().split())
print(h * w - s * w - t * h + s * t)
