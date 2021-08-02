import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


s = SI()
ans = 0
for b in range(1 << (len(s) - 1)):
    f = ""
    for i, c in enumerate(s):
        f += c
        if b >> i & 1: f += "+"
    ans += eval(f)
print(ans)
