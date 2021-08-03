from functools import lru_cache
import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def nn(): return list(stdin.readline().split())
def ns(): return stdin.readline().rstrip()


n = ni()
mod = 10**9 + 7


@lru_cache(maxsize=10000)
def dfs(n, l):
    rt = 0
    if n == 0:
        return 1
    if l[1:3] == 'AG' or l[1:3] == 'GA' or (l[0] == 'A' and l[2] == 'G') or l[:2] == 'AG':
        pass
    else:
        rt += dfs(n - 1, l[1:] + 'C')
    if l[1:] != 'AC':
        rt += dfs(n - 1, l[1:] + 'G')
    rt += dfs(n - 1, l[1:] + 'T')
    rt += dfs(n - 1, l[1:] + 'A')
    return rt % mod


print(dfs(n, 'TTT') % mod)
