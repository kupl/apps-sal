(n, m, i, j, a, b) = list(map(int, input().split()))
ans = 100000000000
if (i, j) == (n, 1) or (i, j) == (1, 1) or (i, j) == (1, m) or ((i, j) == (n, m)):
    print(0)
else:
    hor = i - 1
    ver = j - 1
    if hor % a == 0 and ver % b == 0:
        x = hor // a
        y = ver // b
        if x % 2 == y % 2 and a <= n - 1 and (b <= m - 1):
            ans = min(ans, max(x, y))
    hor = abs(i - n)
    ver = abs(j - m)
    if hor % a == 0 and ver % b == 0:
        x = hor // a
        y = ver // b
        if x % 2 == y % 2 and a <= n - 1 and (b <= m - 1):
            ans = min(ans, max(x, y))
    hor = i - 1
    ver = abs(j - m)
    if hor % a == 0 and ver % b == 0:
        x = hor // a
        y = ver // b
        if x % 2 == y % 2 and a <= n - 1 and (b <= m - 1):
            ans = min(ans, max(x, y))
    hor = abs(n - i)
    ver = j - 1
    if hor % a == 0 and ver % b == 0:
        x = hor // a
        y = ver // b
        if x % 2 == y % 2 and a <= n - 1 and (b <= m - 1):
            ans = min(ans, max(x, y))
    if ans != 100000000000:
        print(ans)
    else:
        print('Poor Inna and pony!')
