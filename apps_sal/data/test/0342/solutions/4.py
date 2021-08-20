(a, b, c) = map(int, input().split())
s = min(a, b)
print(2 * (c + s) + min(1, a - s) + min(1, b - s))
