(a, b) = map(int, input().split())
print(max(a, b) + max(a, b) - 1 if abs(max(a, b) - min(a, b)) >= 2 else max(a, b) + min(a, b))
