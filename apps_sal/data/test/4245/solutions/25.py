a, b = map(int, input().split())

c = b - a
if c % (a - 1) == 0:
    n = c // (a - 1) + 1
else:
    n = c // (a - 1) + 2

print(n)
