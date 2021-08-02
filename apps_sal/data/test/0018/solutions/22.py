#!/usr/bin/pypy3

# s[0] -> t[-1] or t[-1]->u[-1]
# "cab" ->("cab","","")->("ab","c","")->("b","ca","")->("b","c","a")
# 1) stack s->t until min(s).
# 2) passthrough min(s)->u
# min(s,t[-1]) -> u. Repeat.
# need to know the smallest item in s (quickly)
# think it's: split into two subsequences, merge s1(reverse)+s2. minimum.
# "cab" -> s1="cb",s2="a" -> bc
# "dcab" -> "b","dca"
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
