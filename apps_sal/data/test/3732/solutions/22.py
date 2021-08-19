def ag():
    (a, b, m) = list(map(int, input().split()))
    x = min(a, b)
    y = max(a, b)
    res = 0
    if x >= m or y >= m:
        return 0
    elif y <= 0:
        return '-1'
    if x < 0:
        res += int((abs(x) + y - 1) / y)
        x += y * res
    while y < m:
        x1 = y
        y = y + x
        x = x1
        res += 1
    return res


print(ag())
