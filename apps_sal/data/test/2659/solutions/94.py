from math import log10 as l


def s(f):
    return sum(map(int, list(str(f))))


def p(a, j):
    return (a // 10 ** (j + 1) + 1) * 10 ** (j + 1) - 1


n = int(input())
a = 1
for i in range(n):
    print(a)
    if a < 9:
        a += 1
        continue
    a += 1
    k = [p(a, j) for j in range(int(l(a)))]
    o = [p(a, j) / s(p(a, j)) for j in range(int(l(a)))]
    a = k[o.index(min(o))]
