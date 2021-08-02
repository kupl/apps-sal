from itertools import product
import numpy as np

h, w = list(map(int, input().split()))
notwall = []
for _ in range(h):
    s = input()
    notwall.append([int(c == '.') for c in s])

notwall = np.array(notwall)


def getll():
    ls = np.zeros((h, w + 1), dtype=int)

    for i in range(w):
        ls[:, i + 1] = (ls[:, i] + 1) * notwall[:, i]

    ls = ls[:, 1:]
    return ls


def getlr():
    ls = np.zeros((h, w + 1), dtype=int)

    for i in range(w - 1, -1, -1):
        ls[:, i] = (ls[:, i + 1] + 1) * notwall[:, i]

    ls = ls[:, :-1]
    return ls


def getlu():
    ls = np.zeros((h + 1, w), dtype=int)

    for i in range(h):
        ls[i + 1, :] = (ls[i, :] + 1) * notwall[i, :]

    ls = ls[1:, :]
    return ls


def getld():
    ls = np.zeros((h + 1, w), dtype=int)

    for i in range(h - 1, -1, -1):
        ls[i, :] = (ls[i + 1, :] + 1) * notwall[i, :]

    ls = ls[:-1, :]
    return ls


ll = getll()
lr = getlr()
lu = getlu()
ld = getld()

m = max([0, np.max(ll + lr + lu + ld) - 3])

print(m)
