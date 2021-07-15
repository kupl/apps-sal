x, a, b = map(int, input().split())
print("BA"[abs(a - x) < abs(b - x)])
