__author__ = 'alexandrun'
import sys


def process(m, s):
    if s == 0:
        if m == 1:
            return (0, 0)
        return (-1, -1)
    q = s // 9
    r = s % 9
    if r == 0:
        cifMin = q
    else:
        cifMin = q + 1
    if cifMin > m:
        return (-1, -1)
    if cifMin == m:
        if r == 0:
            return ('9' * q, '9' * q)
        min = str(r) + '9' * q
        max = '9' * q + str(r)
        return (min, max)
    if cifMin < m:
        min = '1'
        qmin = (s - 1) // 9
        rmin = (s - 1) % 9
        if rmin == 0:
            cifMin2 = qmin
        else:
            cifMin2 = qmin + 1
        if cifMin2 == m - 1:
            if rmin > 0:
                min += str(rmin) + '9' * qmin
            else:
                min += '9' * qmin
        elif cifMin2 < m - 1:
            if rmin > 0:
                min += '0' * (-cifMin2 + m - 1) + str(rmin) + '9' * qmin
            else:
                min += '0' * (-cifMin2 + m - 1) + '9' * qmin
        max = '9' * q + str(r) + (m - q - 1) * '0'
        return (min, max)


words = input().split()
m = int(words[0])
s = int(words[1])
res = process(m, s)
print(res[0], res[1])
