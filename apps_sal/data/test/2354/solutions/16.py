from math import ceil

n, q = map(int, input().split())
a = []

def getNumber(x, y):
    nonlocal n

    if n % 2 == 0:
        if (x + y) % 2 == 0:
            start = 0
        else:
            start = n ** 2 // 2

        pos = (x - 1) * n // 2 + (y + 1) // 2
    else:
        t = (x - 1) * n + y + 1
        if t % 2 == 0:
            start = 0
        else:
            start = (n ** 2 + 1) // 2
        pos = t // 2
    return start + pos


for i in range(q):
    xi, yi = map(int, input().split())

    a.append(str(getNumber(xi, yi)))

print('\n'.join(a))
