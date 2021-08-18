x, y, m = [int(x) for x in input().split()]
x, y = min(x, y), max(x, y)

if y >= m:
    print(0)
    return

if y <= 0:
    print(-1)
    return

c = 0
if x < 0 and y > 0:
    if m <= 0:
        c = (m - x) // y
    else:
        c = -x // y
    x += c * y

while x < m and y < m:
    xx = x + y
    if xx <= min(x, y):
        print(-1)
        return
    x, y = xx, max(x, y)
    c += 1
print(c)
