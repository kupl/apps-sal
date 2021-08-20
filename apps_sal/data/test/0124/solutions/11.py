def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


(x, y, z) = mi()
(a, b, c) = mi()
ok = 0
if a >= x:
    a -= x
    if a + b >= y:
        if a + b - y + c >= z:
            ok = 1
print('YES' if ok else 'NO')
