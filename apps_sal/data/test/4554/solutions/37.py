w, a, b = map(int, input().split())
if a > b:
    a, b = b, a
print(max(0, b - a - w))
