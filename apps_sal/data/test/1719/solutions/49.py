import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n = ni()
mod = 10**9+7
from functools import lru_cache

@lru_cache(maxsize=1000)
def dfs(n, l):
    rt = 0
    if n == 0:
        return 1
    if l[1:3] == 'AG' or l[1:3] == 'GA' or (l[0] == 'A' and l[2] == 'G') or l[:2] == 'AG':
        pass
    else:
        rt += dfs(n-1, l[1:]+'C')
    if l[1:] != 'AC':
        rt += dfs(n-1,l[1:]+'G')
    rt += dfs(n-1,l[1:]+'T')
    rt += dfs(n-1,l[1:]+'A')
    return rt%mod



print(dfs(n,'TTT')%mod)
