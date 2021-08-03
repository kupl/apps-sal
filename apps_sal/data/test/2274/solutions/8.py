from collections import *
from sys import stdin, stderr


def rl():
    return [int(w) for w in stdin.readline().split()]


t, = rl()
for _ in range(t):
    n, m = rl()
    a = [stdin.readline().rstrip() for _ in range(n)]
    r = 0
    for c in a[-1]:
        if c == 'D':
            r += 1
    for l in a:
        if l[-1] == 'R':
            r += 1
    print(r)
