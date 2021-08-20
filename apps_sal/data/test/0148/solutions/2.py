(n, a, x, b, y) = list(map(int, input().split()))
a -= 1
x -= 1
b -= 1
y -= 1
while True:
    if a == b:
        print('YES')
        break
    if a == x or b == y:
        print('NO')
        break
    a = (a + 1) % n
    b = (b - 1) % n
