from collections import defaultdict


def f(n):
    st = 0
    while n % 2 == 0:
        n //= 2
        st += 1
    return n, st


t = int(input())
for _ in range(t):
    n = int(input())
    d = defaultdict(int)
    for i in input().split():
        el = int(i)
        os, st = f(el)
        d[os] = max(d[os], st)
    s = 0
    for el in list(d.values()):
        s += el
    print(s)

