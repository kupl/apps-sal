(a, b, k) = map(int, input().split())
print(a - k, b) if k <= a else print(0, b - (k - a)) if k <= a + b else print(0, 0)
