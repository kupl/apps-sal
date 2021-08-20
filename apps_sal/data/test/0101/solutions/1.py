n = int(input())
a = int(input())
b = int(input())
x = 0
y = -1
while a * x <= n:
    if (n - a * x) % b == 0:
        y = (n - a * x) // b
        break
    x += 1
if y == -1:
    print('NO')
else:
    print('YES')
    print(x, y, sep=' ')
