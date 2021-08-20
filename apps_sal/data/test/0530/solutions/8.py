import sys
import bisect
try:
    fin = open('in')
except:
    fin = sys.stdin


def input():
    return fin.readline().strip()


n = int(input())
a = list(map(int, input()))
b = list(map(int, input()))
r = [[0, 0], [0, 0]]
for i in range(2 * n):
    r[a[i]][b[i]] += 1
t = [0] * 2
for i in range(2 * n):
    j = i % 2
    if r[1][1] > 0:
        r[1][1] -= 1
        t[j] += [1, 1][j]
    elif r[0][1] > 0:
        r[0][1] -= 1
        t[j] += [0, 1][j]
    elif r[1][0] > 0:
        r[1][0] -= 1
        t[j] += [1, 0][j]
    else:
        r[0][0] -= 1
        t[j] += [0, 0][j]
(x, y) = t
if x > y:
    print('First')
elif x < y:
    print('Second')
else:
    print('Draw')
