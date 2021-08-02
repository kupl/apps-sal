W, a, b = list(map(int, input().split()))

print((max(abs(b - a) - W, 0)))
