import sys
from collections import *

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

n = int(input())
pp = LI()
xx = LI()
to = defaultdict(list)
ww = [[-1, -1] for _ in range(n)]

def dfs(u=0):
    if not len(to[u]):
        ww[u] = [xx[u], 0]
        return True
    ret_ww = set([0])
    uw = xx[u]
    sum_ret_w = 0
    for cu in to[u]:
        if not dfs(cu): return False
        new_ret_ww = set()
        for cuw in ww[cu]:
            sum_ret_w += cuw
            for ret_w in ret_ww:
                new_ret_w = ret_w + cuw
                if new_ret_w <= uw: new_ret_ww.add(new_ret_w)
        ret_ww = new_ret_ww
    if not ret_ww: return False
    ww[u] = [uw, sum_ret_w - max(ret_ww)]
    return True

def main():
    for u, p in enumerate(pp, 1):
        to[p - 1].append(u)
    # print(to)
    if dfs():
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
    # print(ww)

main()

