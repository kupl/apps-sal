from heapq import *
import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


def main():
    def dfs(i):
        res = 1
        for j in to[i]:
            res = res * dfs(j) % md
        return res + 1

    md = 998244353
    n = II()
    xd = LLI(n)
    xd.sort(reverse=True)
    to = [[] for _ in range(n)]
    hp = []
    for i, (x, d) in enumerate(xd):
        while hp and hp[0][0] < x + d:
            px, pi = heappop(hp)
            to[i].append(pi)
        heappush(hp, (x, i))
    ans = 1
    while hp:
        _, i = heappop(hp)
        ans = ans * dfs(i) % md
    print(ans)


main()
