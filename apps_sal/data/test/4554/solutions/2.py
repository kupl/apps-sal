(w, a, b) = map(int, input().split())
print(max(0, b - a - w) if b >= a else max(0, a - b - w))
