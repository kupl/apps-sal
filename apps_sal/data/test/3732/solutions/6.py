def change(x, y):
    if x > y:
        tmp = y
        y = x
        x = tmp
    return (x, y)


(x, y, m) = [int(x) for x in input().split()]
if x >= m or y >= m:
    ans = 0
elif x <= 0 and y <= 0:
    ans = -1
else:
    ans = 0
    (x, y) = change(x, y)
    if x < 0:
        ans = int(-x / y)
        ans += 1
        x = y - -x % y
    while y < m:
        tmp = x + y
        x = y
        y = tmp
        (x, y) = change(x, y)
        ans += 1
print(ans)
