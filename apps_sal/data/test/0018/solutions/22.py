
from sys import stdin, stderr


def readInts(): return map(int, stdin.readline().strip().split())
def print_err(*args, **kwargs): print(*args, file=stderr, **kwargs)


def solve(s):
    s = list(s)
    sn = len(s)
    pq = sorted(zip(list(s), range(sn)))
    ix_left = 0
    u, v = [], []
    for c, ix in pq:
        if ix < ix_left:
            continue
        while u and c >= u[-1]:
            v.append(u.pop())
        for cix in range(ix_left, ix + 1):
            u.append(s[cix])
        ix_left = ix + 1
    while u:
        v.append(u.pop())
    return v


def run():
    s = input().strip()
    print("".join(solve(s)))


run()
