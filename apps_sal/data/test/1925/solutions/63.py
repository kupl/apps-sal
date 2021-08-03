a, b, n = map(int, input().split())

x = min(b - 1, n) * 1.0

print(int(1.0 * a * x / b) - a * int(1.0 * x / b))
