(x, y, z) = map(int, input().split())
(a, b, c) = map(int, input().split())
if a + b + c < x + y + z:
    print('NO')
    quit()
if a < x:
    print('NO')
    quit()
a -= x
if a + b < y:
    print('NO')
    quit()
print('YES')
