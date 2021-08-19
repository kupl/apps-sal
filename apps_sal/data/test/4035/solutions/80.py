(a, b) = map(int, input().split())
x = min([n if (n * 0.08 // 1 - a, n * 0.1 // 1 - b) == (0, 0) else 100000.0 for n in range(1500)])
print(x if x < 100000.0 else -1)
