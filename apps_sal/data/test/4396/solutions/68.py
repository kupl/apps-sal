n = int(input())
(j, b) = (0, 0)
for _ in range(n):
    (x, y) = input().split()
    x = float(x)
    if y == 'JPY':
        j += x
    else:
        b += x
print(j + b * 380000)
