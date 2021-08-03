a, b = map(int, input().split())
x = y = z = 0
while a % 2 == 0:
    x += 1
    a //= 2
while a % 3 == 0:
    y += 1
    a //= 3
while a % 5 == 0:
    z += 1
    a //= 5
while b % 2 == 0:
    x -= 1
    b //= 2
while b % 3 == 0:
    y -= 1
    b //= 3
while b % 5 == 0:
    z -= 1
    b //= 5
print(abs(x) + abs(y) + abs(z) if a == b else -1)
