def Solve():
    (x, y, m) = list(map(int, input().split()))
    if x >= m or y >= m:
        return 0
    if x <= 0 and y <= 0:
        return -1
    ans = 0
    if y <= 0:
        ans = abs(y) // x + 1
        y += ans * x
    elif x <= 0:
        ans = abs(x) // y + 1
        x += ans * y
    while x < m and y < m:
        if x < y:
            x += y
        else:
            y += x
        ans += 1
    return ans


print(Solve())
