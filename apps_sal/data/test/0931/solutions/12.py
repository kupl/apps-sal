from sys import stdin


def arr_inp(n):
    if n == 1:
        return [int(x) for x in stdin.readline().split()]
    elif n == 2:
        return [float(x) for x in stdin.readline().split()]
    else:
        return [str(x) for x in stdin.readline().split()]


def clockwise(mod):
    for i in range(1, mod + 1):
        for j in range(p):
            if i & 1:
                a[j] = [a[j][1], (n + 1) - a[j][0]]
            else:
                a[j] = [a[j][1], (m + 1) - a[j][0]]


def horizontal(mod):
    if mod:
        for i in range(p):
            if x & 1:
                a[i][1] = (n + 1) - a[i][1]
            else:
                a[i][1] = (m + 1) - a[i][1]


def counter(mod):
    for i in range(1, mod + 1):
        for j in range(p):
            if x % 2:
                if i & 1:
                    a[j] = [a[j][1], (m + 1) - a[j][0]]
                else:
                    a[j] = [a[j][1], (n + 1) - a[j][0]]
            else:
                if i & 1:
                    a[j] = [a[j][1], (n + 1) - a[j][0]]
                else:
                    a[j] = [a[j][1], (m + 1) - a[j][0]]


def print1():
    for i in range(p):
        print(*a[i])


n, m, x, y, z, p = arr_inp(1)
a = [arr_inp(1) for i in range(p)]
# print(x % 4, y % 2, z % 4)

clockwise(x % 4)
horizontal(y % 2)
if z % 4 > 0:
    counter(4 - (z % 4))
print1()
