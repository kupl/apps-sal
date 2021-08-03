import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

s = I()
vs = set()
vs.add(s)
now = 0 + s
i = 1
while True:
    i += 1
    now = now / 2 if now % 2 == 0 else 3 * now + 1
    if now in vs:
        break
    else:
        vs.add(now)

print(i)
