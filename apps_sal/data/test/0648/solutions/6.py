m, b = map(int, input().split(" "))
sm = 0
for y in range(0, b + 1):
    x = m * (b - y)
    s = (x + y) * (x + 1) * (y + 1) // 2
    sm = max(s, sm)
print(sm)
