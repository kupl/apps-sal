import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n,z,w = na()
a = na()

if n == 1:
    print(abs(a[-1]-w))
    return

print(max(abs(a[-1]-w),abs(a[-2]-a[-1])))
