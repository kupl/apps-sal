from math import sin


def mp():
    return list(map(int, input().split()))


def lt():
    return list(map(int, input().split()))


def pt(x):
    print(x)


def ip():
    return input()


def it():
    return int(input())


def sl(x):
    return [t for t in x]


def spl(x):
    return x.split()


def aj(liste, item):
    liste.append(item)


def bin(x):
    return '{0:b}'.format(x)


def listring(l):
    return ' '.join([str(x) for x in l])


def ptlist(l):
    print(' '.join([str(x) for x in l]))


n = it()
step = lt()
dict = {}


def explosion(start, s, d):
    (i, j) = start
    t = s + 1
    if d == 0:
        for k in range(j + 1, j + t):
            dict[i, k] = True
        return (((i, j + t - 1), (d + 7) % 8), ((i, j + t - 1), (d + 1) % 8))
    if d == 1:
        for k in range(1, t):
            dict[i + k, j + k] = True
        return (((i + t - 1, j + t - 1), (d + 7) % 8), ((i + t - 1, j + t - 1), (d + 1) % 8))
    if d == 2:
        for k in range(1, t):
            dict[i + k, j] = True
        return (((i + t - 1, j), (d + 7) % 8), ((i + t - 1, j), (d + 1) % 8))
    if d == 3:
        for k in range(1, t):
            dict[i + k, j - k] = True
        return (((i + t - 1, j - t + 1), (d + 7) % 8), ((i + t - 1, j - t + 1), (d + 1) % 8))
    if d == 4:
        for k in range(1, t):
            dict[i, j - k] = True
        return (((i, j - t + 1), (d + 7) % 8), ((i, j - t + 1), (d + 1) % 8))
    if d == 5:
        for k in range(1, t):
            dict[i - k, j - k] = True
        return (((i - t + 1, j - t + 1), (d + 7) % 8), ((i - t + 1, j - t + 1), (d + 1) % 8))
    if d == 6:
        for k in range(1, t):
            dict[i - k, j] = True
        return (((i - t + 1, j), (d + 7) % 8), ((i - t + 1, j), (d + 1) % 8))
    if d == 7:
        for k in range(1, t):
            dict[i - k, j + k] = True
        return (((i - t + 1, j + t - 1), (d + 7) % 8), ((i - t + 1, j + t - 1), (d + 1) % 8))


start = [((0, 0), 0)]
for i in range(n):
    l = []
    for (p, q) in start:
        (a, b) = explosion(p, step[i], q)
        l.append(a)
        l.append(b)
    start = set(l)
pt(len(dict))
