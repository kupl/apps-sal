import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N,K = map(int,input().split())
AB = [tuple(map(int,input().split())) for i in range(N-1)]

es = [[] for _ in range(N)]
for a,b in AB:
    a,b = a-1,b-1
    es[a].append(b)
    es[b].append(a)

MOD = 10**9+7
ans = K
def rec(v,p=-1,d=0):
    nonlocal ans
    k = K-2 if d else K-1
    for to in es[v]:
        if to==p: continue
        ans *= k
        ans %= MOD
        k -= 1
        rec(to,v,d+1)
rec(0)
print(ans)
