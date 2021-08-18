n = int(input())
x = 1234567
y = 123456
z = 1234
for a in range(900):
    if a * x > n:
        break
    for b in range(9000):
        if a * x + b * y > n:
            break
        c = (n - a * x - b * y) // z
        if a * x + b * y + c * z == n:
            print('YES')
            return
print('NO')
