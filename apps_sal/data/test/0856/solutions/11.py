from queue import Queue


def rn():
    a = int(input())
    return a


def rl():
    a = list(map(int, input().split()))
    return a


for _ in range(rn()):
    [n, k] = rl()
    a = rl()
    b = a.copy()
    c = max(a)
    for i in range(n):
        b[i] = c - b[i]
    c = max(b)
    d = b.copy()
    for i in range(n):
        d[i] = c - d[i]
    if k % 2 == 0:
        print(*d)
    else:
        print(*b)
