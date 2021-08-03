import sys

sys.setrecursionlimit(10 ** 5)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


for _ in range(II()):
    n = II()
    aa = LI()
    if aa[0] + aa[1] > aa[-1]:
        print(-1)
    else:
        print(1, 2, n)
