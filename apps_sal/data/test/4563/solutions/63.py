n = int(input())
ca, cb = 0, 0
for i in range(n):
    a, b = list(map(int, input().split()))
    x, y = 1, 1
    if ca > a:
        x = ca // a
        if ca % a:
            x += 1
    if cb > b:
        y = cb // b
        if cb % b:
            y += 1
    x = max(x, y)
    ca = a * x
    cb = b * x
print((ca + cb))
