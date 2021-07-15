# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def fi(): return float(input())
def mfi(): return map(float, input().rstrip().split())
def lmfi(): return list(map(float, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
def exit(*arg): print(*arg); return
# template


def main():
    t = ii()
    for _ in range(t):
        n = ii()
        p = lmi()
        m = ii()
        q = lmi()
        op = 0
        oq = 0
        ep = 0
        eq = 0
        for x in p:
            if x % 2 == 0:
                ep += 1
            else:
                op += 1
        for x in q:
            if x % 2 == 0:
                eq += 1
            else:
                oq += 1
        print(op * oq + ep * eq)
    return


def __starting_point():
    main()

__starting_point()
