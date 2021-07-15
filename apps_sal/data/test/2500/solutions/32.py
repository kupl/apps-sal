import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def f(x, s):
    if min(x, s) < 0: return 0
    if max(x, s) < 2:
        if x and s: return 2
        else: return 1
    if (x, s) in memo: return memo[x, s]
    res = f(x >> 1, s >> 1) + f(x - 1 >> 1, s - 1 >> 1) + f(x >> 1, s - 2 >> 1)
    res = memo[x, s] = res % md
    return res

memo = {}
md = 10 ** 9 + 7

def main():
    n = II()
    print(f(n, n))

main()

