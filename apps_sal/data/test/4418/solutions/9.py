n = int(input())
arr = list(map(int, input().split()))
(_4, _8, _15, _16, _23, _42) = (0, 0, 0, 0, 0, 0)
for i in arr:
    if i == 4:
        _4 += 1
    if i == 8 and _4 > _8:
        _8 += 1
    elif i == 15 and _8 > _15:
        _15 += 1
    elif i == 16 and _15 > _16:
        _16 += 1
    elif i == 23 and _16 > _23:
        _23 += 1
    elif i == 42 and _23 > _42:
        _42 += 1
print(n - _42 * 6)
