ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

x, y, z = mi()
a, b, c = mi()
ok = 0
if a >= x:
    a -= x
    if a + b >= y:
        if a + b - y + c >= z:
            ok = 1
print('YES' if ok else 'NO')
