import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def solve():
    N = int(input())
    AB = [tuple(map(int,input().split())) for i in range(N-1)]
    es = [[] for i in range(N)]
    for i,(a,b) in enumerate(AB):
        a,b = a-1,b-1
        es[a].append((b,i))
        es[b].append((a,i))
    MOD = 10**9+7

    size = [-1] * N
    def calc_size(v,p=-1):
        ret = 1
        for to,_ in es[v]:
            if to==p: continue
            ret += calc_size(to,v)
        size[v] = ret
        return ret
    calc_size(0)

    MAXN = N+5
    fac = [1,1] + [0]*MAXN
    finv = [1,1] + [0]*MAXN
    inv = [0,1] + [0]*MAXN
    for i in range(2,MAXN+2):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = -inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD

    dpdn = [0] * (N-1)
    dn = set()
    def dfs(v,p=-1):
        ret = fac[size[v]-1]
        for to,i in es[v]:
            if to==p: continue
            dn.add((v,to))
            dpdn[i] = dfs(to,v)
            ret *= finv[size[to]] * dpdn[i]
        ret %= MOD
        return ret
    dfs(0)

    dpup = [0] * (N-1)
    from collections import deque
    q = deque([(0,-1)])
    while q:
        v,p = q.popleft()
        whole = 1
        for to,i in es[v]:
            if to != p:
                whole *= finv[size[to]] * dpdn[i]
            else:
                whole *= finv[N-size[v]] * dpup[i]
        whole %= MOD
        for to,i in es[v]:
            if to==p: continue
            dpup[i] = (whole * fac[N-size[to]-1] * fac[size[to]] * pow(dpdn[i], MOD-2, MOD)) % MOD
            q.append((to,v))

    ans = []
    for v in range(N):
        a = 1
        s = 0
        for to,i in es[v]:
            if (v,to) in dn:
                s += size[to]
                a *= finv[size[to]] * dpdn[i]
            else:
                s += N-size[v]
                a *= finv[N-size[v]] * dpup[i]
            a %= MOD
        a *= fac[s]
        ans.append(a%MOD)
    print(*ans, sep='\n')

solve()
