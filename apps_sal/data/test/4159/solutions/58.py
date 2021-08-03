a, b, k = map(int, input().split())
print(min(a, max(a - k, 0)), min(b, max(b - k + a, 0)))
