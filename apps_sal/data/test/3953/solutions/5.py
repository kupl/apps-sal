from sys import stdin
__author__ = 'artyom'


def solve(x):
    a = []
    for s in x:
        dot_pos = s.find('.')
        if dot_pos < 0:
            return None
        a.append(dot_pos + 1)
    return a


def rotate(x, n):
    y = []
    for i in range(n):
        y.append([])
        for j in range(n):
            y[i].append(x[j][i])
    return map(lambda b: ''.join(b), y)


n = int(stdin.readline().strip())
x = []
for _ in range(n):
    x.append(stdin.readline().strip())
a = solve(x)
if a:
    for i in range(n):
        print(i + 1, a[i])
else:
    a = solve(rotate(x, n))
    if a:
        for i in range(n):
            print(a[i], i + 1)
    else:
        print(-1)
