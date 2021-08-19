from collections import defaultdict as dd
from sys import stdin
input = stdin.buffer.readline


def I():
    return list(map(int, input().split()))


(n,) = I()
l = []
d = dd(int)
su = dd(int)
s = 0
an = [1, 1, 2, 1]
for i in range(n):
    l.append(I())
    for j in range(n):
        d[i - j] += l[i][j]
        su[i + j] += l[i][j]
x = 0
y = 0
for i in range(n):
    for j in range(n):
        l[i][j] = d[i - j] + su[i + j] - l[i][j]
        if (i + j) % 2:
            if l[i][j] > x:
                (an[0], an[1]) = (i + 1, j + 1)
                x = l[i][j]
        elif l[i][j] > y:
            (an[2], an[3]) = (i + 1, j + 1)
            y = l[i][j]
s = x + y
print(s)
print(*an)
