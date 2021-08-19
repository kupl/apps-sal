(a, b) = map(int, input().split())
maximum = max(a + b, a - b, a * b)
print(maximum)
