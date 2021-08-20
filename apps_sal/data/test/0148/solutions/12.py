(n, a, x, b, y) = map(int, input().split())
a -= 1
b -= 1
x -= 1
y -= 1
res = a == b
while a != x and b != y:
    if a != x:
        a = (a + 1) % n
    if b != y:
        b = (b - 1) % n
    res |= a == b
print('YES' if res else 'NO')
