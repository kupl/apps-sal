x, y, m = (int(q) for q in input().split())
if x >= m or y >= m:
    print(0)
    return
if x <= 0 and y <= 0:
    print(-1)
    return
ans = 0
if x < 0:
    ans += -x // y
    x += -x // y * y
if y < 0:
    ans += -y // x
    y += -y // x * x
while x < m and y < m:
    ans += 1
    if x < y:
        x += y
    else:
        y += x
print(ans)
