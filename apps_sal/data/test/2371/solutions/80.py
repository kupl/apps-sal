import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def nn(): return list(stdin.readline().split())
def ns(): return stdin.readline().rstrip()


n, z, w = na()
a = na()

if n == 1:
    print(abs(a[-1] - w))
    return

print(max(abs(a[-1] - w), abs(a[-2] - a[-1])))
