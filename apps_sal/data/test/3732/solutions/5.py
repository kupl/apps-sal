s = input().split()
(x, y, m) = (int(i) for i in s)
ans = 0
if x >= m or y >= m:
    print(0)
elif x <= 0 and y <= 0:
    print(-1)
else:
    if x < 0:
        q = abs(x // y)
        ans += q
        x += y * q
    elif y < 0:
        q = abs(y // x)
        ans += q
        y += x * q
    while x < m and y < m:
        ans += 1
        if x < y:
            x = x + y
        else:
            y = x + y
    print(ans)
