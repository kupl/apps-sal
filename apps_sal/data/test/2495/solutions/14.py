n = int(input())
a = list(map(int, input().split()))
(x, y, z) = (0, 0, 0)
for i in range(n):
    x += a[i]
    if i % 2 == 0:
        if x > 0:
            pass
        else:
            y += 1 - x
            x = 1
    elif x < 0:
        pass
    else:
        y += x + 1
        x = -1
x = 0
for i in range(n):
    x += a[i]
    if i % 2 == 1:
        if x > 0:
            pass
        else:
            z += 1 - x
            x = 1
    elif x < 0:
        pass
    else:
        z += x + 1
        x = -1
print(min(y, z))
