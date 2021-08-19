(p, k) = input().split()
p = int(p)
k = int(k)
y = 10 * k - 1
x = (10 ** (p - 1) - k) % y
b = True
for i in range(k, 10):
    if x * i % y == 0:
        z = i * 10
        while (z - i) % y:
            z *= 10
        part = str((z - i) // y)
        print(part * (p // len(part)))
        b = False
        break
if b:
    print('Impossible')
