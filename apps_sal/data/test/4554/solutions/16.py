(w, a, b) = map(int, input().split())
print(max(0, b - a - w, a - b - w))
