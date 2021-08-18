import sys
from math import sqrt, sin, cos, pi
from collections import defaultdict as dd, deque, Counter as C

mod = pow(10, 9) + 7
mod2 = 998244353


def data(): return sys.stdin.readline().strip()


def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var)) + end)


def l(): return list(sp())


def sl(): return list(ssp())


def sp(): return list(map(int, data().split()))


def ssp(): return list(map(str, data().split()))


def l1d(n, val=0): return [val for i in range(n)]


def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]


for _ in range(int(data())):
    n = int(data())
    arr = l()
    even, odd = [], []
    for i in range(n):
        if arr[i] & 1:
            odd.append(arr[i])
            continue
        even.append(arr[i])
    if not(len(odd) & 1):
        out("YES")
        continue
    r = False
    for i in odd:
        for j in even:
            if abs(i - j) == 1:
                r = True
                break
        if r:
            break
    if r:
        out("YES")
        continue
    out("NO")
