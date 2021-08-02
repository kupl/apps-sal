import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())


sys.setrecursionlimit(10**9)

a, b, x, y = mapint()

if a > b:
    n = a - b
    print(min((n - 1) * y + x, (x * 2) * n - x))
else:
    n = b - a
    print(min(n * y + x, (x * 2) * n + x))
