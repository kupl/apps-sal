import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
fac = [-1] * (10**6+1)
inv = [-1] * (10**6+1)
finv = [-1] * (10**6+1)

fac[0] = fac[1] = 1
inv[1] = 1
finv[0] = finv[1] = 1

def initNCMMod(limit):
    for i in range(2, limit):
        fac[i] = fac[i-1] * i % mod
        inv[i] = mod - inv[mod%i] * (mod // i) % mod
        finv[i] = finv[i-1] * inv[i] % mod

def NCMMod(n, k):
    if n < k:
        return 0
    if (n < 0 or k < 0):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod
initNCMMod(10**5+1)

def P(n, k):
    return (fac[n] * finv[n-k]) % mod

def main():
    N, K = LI()
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = LI_()
        G[a].append(b)
        G[b].append(a)
    q = deque([])
    q.append((0, -1, True))
    ans = K
    while q:
        v, par, is_root = q.popleft()
        n_child = len(G[v])
        remain_color = K - 1

        if not is_root:
            remain_color -= 1
            n_child -= 1

        for next_v in G[v]:
            if next_v == par:
                continue
            q.append((next_v, v, False))

        if n_child <= remain_color:
            ans *= P(remain_color, n_child)
            ans %= mod
        else:
            ans = 0
            break

    print(ans)

main()


