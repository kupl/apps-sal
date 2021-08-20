def read(type=1):
    if type:
        file = open('input.dat', 'r')
        n = int(file.readline())
        a = []
        for i in range(n):
            a.append(int(file.readline()))
        file.close()
    else:
        n = int(input().strip())
        a = []
        for i in range(n):
            a.append(int(input().strip()))
    return (n, a)


def check():
    s = 0
    for i in range(n):
        if c[i]:
            s += a[i]
        else:
            s -= a[i]
    if s % 360 == 0:
        return 1


def back():
    if len(c) == n:
        if check():
            return 1
    else:
        for i in range(2):
            c.append(i)
            if back():
                return 1
            c.pop()


def solve():
    if back():
        return 1
    else:
        return 0


c = []
(n, a) = read(0)
if solve():
    print('YES')
else:
    print('NO')
