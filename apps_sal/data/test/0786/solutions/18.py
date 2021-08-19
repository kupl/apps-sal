# Author: Maharshi Gor
import sys

sys.setrecursionlimit(5000000)


def read(type=int):
    return type(input())


def read_arr(type=int):
    return [type(token) for token in input().split()]


def abs(num):
    return num if num > 0 else -num


inf = 10 ** 9

c = 1899

u, l = inf, -inf
diff = 0
n = read()
A = []
for i in range(n):
    r, d = read_arr()
    A.append((r, d))

e = False
for r, d in A:
    if d == 1:
        l = max(l, 1900 - diff)
    else:
        u = min(u, 1899 - diff)
    # print(diff, d, l, u)
    diff += r
    if u < l:
        e = True
        break


if e or l > u:
    print("Impossible")
elif u == inf:
    print("Infinity")
else:
    print(u + diff)
