(x, y, z) = map(int, input().split())
(a, b, c) = map(int, input().split())
res = True
if a >= x:
    a -= x
    if a + b >= y:
        if a + b + c - y >= z:
            res = True
        else:
            res = False
    else:
        res = False
else:
    res = False
print('YES' if res else 'NO')
