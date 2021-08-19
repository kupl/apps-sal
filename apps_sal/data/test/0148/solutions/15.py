(n, a, x, b, y) = list(map(int, input().split()))
a -= 1
x -= 1
b -= 1
y -= 1
while a != x and b != y:
    if a == b:
        print('YES')
        raise SystemExit(0)
    a = (a + 1) % n
    b = (b - 1 + n) % n
if a == b:
    print('YES')
else:
    print('NO')
