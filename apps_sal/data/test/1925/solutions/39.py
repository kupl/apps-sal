(a, b, n) = list(map(int, input().split()))
print(int(a * min(n, b - 1) / b) - a * int(min(n, b - 1) / b))
