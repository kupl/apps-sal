import re


def maxString(a, i, n):
    s2 = ''.join(a[i])
    if '1' not in s2:
        return 0
    r = len(max(re.findall("1+", s2), key=len))
    return r


def flip(x):
    if(x == '1'):
        return '0'
    else:
        return '1'


n, m, q = map(int, input().split())

a = []
x = []

for i in range(n):
    x = list(input().split())
    a.append(x)

y = []

for i in range(n):
    y.append(maxString(a, i, n))

z = max(y)
r = y.index(z)

for i in range(q):
    x1, y1 = map(int, input().split())
    a[x1 - 1][y1 - 1] = flip(a[x1 - 1][y1 - 1])
    y[x1 - 1] = maxString(a, x1 - 1, n)
    z = max(y)
    print(z)
