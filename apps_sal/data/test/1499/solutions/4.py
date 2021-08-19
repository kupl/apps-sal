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


(n, m) = mp()
if m <= 2 * n:
    print(' '.join([str(i + 1) for i in range(m)]))
else:
    d = (m - 2 * n) // 2
    L = []
    for i in range(d):
        L += [2 * n + 2 * i + 1, 2 * i + 1, 2 * n + 2 * i + 2, 2 * i + 2]
    c = m - 2 * n - 2 * d
    if c == 1:
        L.append(m)
    for i in range(d, n):
        L += [2 * i + 1, 2 * i + 2]
    print(' '.join([str(x) for x in L]))
