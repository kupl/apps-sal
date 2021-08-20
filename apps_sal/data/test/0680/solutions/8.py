(x1, y1) = list(map(int, input().split()))
(x2, y2) = list(map(int, input().split()))
(x3, y3) = list(map(int, input().split()))
a = [[x1, y1], [x2, y2], [x3, y3]]
a.sort()
ans = []
if a[1][1] <= a[2][1]:
    x = a[1][0]
    y = a[1][1]
    while y <= a[2][1]:
        ans += [[x, y]]
        y += 1
    y -= 1
    x += 1
    while x <= a[2][0]:
        ans += [[x, y]]
        x += 1
else:
    x = a[1][0]
    y = a[1][1]
    while y >= a[2][1]:
        ans += [[x, y]]
        y -= 1
    y += 1
    x += 1
    while x <= a[2][0]:
        ans += [[x, y]]
        x += 1
if a[1][1] <= a[0][1]:
    x = a[1][0]
    y = a[1][1]
    while y <= a[0][1]:
        if [x, y] not in ans:
            ans += [[x, y]]
        y += 1
    y -= 1
    x -= 1
    while x >= a[0][0]:
        if [x, y] not in ans:
            ans += [[x, y]]
        x -= 1
else:
    x = a[1][0]
    y = a[1][1]
    while y >= a[0][1]:
        if [x, y] not in ans:
            ans += [[x, y]]
        y -= 1
    y += 1
    x -= 1
    while x >= a[0][0]:
        if [x, y] not in ans:
            ans += [[x, y]]
        x -= 1
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])
