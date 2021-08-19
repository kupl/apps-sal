n = int(input())
(a, b) = input().split(' ')
(a, b) = (int(a), int(b))
m = max(a, b)
bol = True
for i in range(n - 1):
    (x, y) = input().split(' ')
    (x, y) = (int(x), int(y))
    if max(x, y) <= m:
        m = max(x, y)
    elif min(x, y) <= m:
        m = min(x, y)
    else:
        bol = False
if bol:
    print('YES')
else:
    print('NO')
