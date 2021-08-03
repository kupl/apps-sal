x, y = input().split()
x = int(x)
y = int(y)
p, q, z, i, j = 0, 0, 0, 1, 1


def GT(n):
    t = 0
    for i in range(1, n + 1):
        if(i % 2 != 0):
            t += i
        else:
            t += (-i)
    return t


while (1):
    x1, y1 = max(GT(i), GT(i - 1)), min(GT(i), GT(i - 1))
    x2, y2 = max(GT(j), GT(j - 1)), min(GT(j), GT(j - 1))
    if(z % 2 == 0):
        p = GT(i)
        i += 1
    if(z % 2 != 0):
        q = GT(j)
        j += 1
    z += 1
    if(x >= y1 and x <= x1 and y == q):
        break
    if(y >= y2 and y <= x2 and x == p):
        break
if((x == 0 and y == 0) or (x == 1 and y == 0)):
    print(0)
else:
    print(z)
