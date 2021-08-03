from sys import *

n = int(stdin.readline())

INF = 100000000000000000000000
MAX = 2 * INF
MIN = - MAX
possible = True

for _ in range(n):
    c, d = stdin.readline().split(' ')
    c = int(c)
    d = int(d)

    if d is 1:
        MIN = max(MIN, 1900)
    if d is 2:
        MAX = min(MAX, 1899)

    if MIN > MAX:
        possible = False

    MIN += c
    MAX += c

if not possible:
    print('Impossible')
else:
    if MAX > INF:
        print('Infinity')
    else:
        print(MAX)
