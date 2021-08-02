a, b, x, y = map(int, input().split())
t = 0
if a > b:
    c = (a - 1) - b
else:
    c = b - a
t += x
if x * 2 < y:
    t += c * x * 2
else:
    t += c * y
print(t)
