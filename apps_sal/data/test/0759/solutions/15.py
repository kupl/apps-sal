hh, mm = map(int, input().split())
h, d, c, n = map(int, input().split())
x = (h + n - 1) // n * c
y = (h + d * max(0, 20 * 60 - (hh * 60 + mm)) + n - 1) // n * c * 0.8
print(min(x, y))
