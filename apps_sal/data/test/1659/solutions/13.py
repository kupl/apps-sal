n, x = map(int, input().split())
nb = 0
for _ in range(n):
    a, b = input().split()
    b = int(b)
    if a == '+':
        x += b
    else:
        if b <= x:
            x -= b
        else:
            nb += 1
print(x, nb)
