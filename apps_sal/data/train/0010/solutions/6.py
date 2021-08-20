from collections import *
from sys import stdin, stderr


def rl():
    return [int(w) for w in stdin.readline().split()]


(t,) = rl()
for _ in range(t):
    (n,) = rl()
    p = rl()
    s = [p[0]]
    for i in range(1, n - 1):
        if p[i - 1] < p[i] > p[i + 1] or p[i - 1] > p[i] < p[i + 1]:
            s.append(p[i])
    s.append(p[-1])
    print(len(s))
    print(*s)
