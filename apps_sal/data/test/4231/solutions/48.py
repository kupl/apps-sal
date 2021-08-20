(a, b) = map(int, input().split())
(h, w) = map(int, input().split())
print(a * b - (h * b + a * w - w * h))
