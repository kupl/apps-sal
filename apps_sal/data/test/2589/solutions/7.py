from collections import *
from sys import stdin,stderr
def rl():
    return [int(w) for w in stdin.readline().split()]

t, = rl()
for _ in range(t):
    n, x = rl()
    a = rl()
    if sum(a) % x:
        print(n)
    else:
        good_i = [i for (i, y) in enumerate(a) if y % x]
        if good_i:
            print(max(n - 1 - min(good_i), max(good_i)))
        else:
            print(-1)

