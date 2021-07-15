import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import defaultdict

N, K, L = list(map(int, input().split()))
G1 = [[] for i in range(N)]
for i in range(K):
    p, q = list(map(int, input().split()))
    p -= 1
    q -= 1
    G1[p].append(q)
    G1[q].append(p)
gids = [0]*N
done = [False]*N
def dfs1(i, gid):
    gids[i] = gid
    done[i] = True
    for nex in G1[i]:
        if done[nex]: continue
        dfs1(nex, gid)
gid = 0
for i in range(N):
    if not done[i]:
        dfs1(i, gid)
        gid += 1

G = [[] for i in range(N)]
for i in range(L):
    r, s = list(map(int, input().split()))
    r -= 1
    s -= 1
    G[r].append(s)
    G[s].append(r)
done = [False]*N
D = []
gid = 0
def dfs(i, gid):
    D[gid][gids[i]] += 1
    done[i] = True
    for nex in G[i]:
        if done[nex]: continue
        dfs(nex, gid)
for i in range(N):
    if not done[i]:
        D.append(defaultdict(int))
        dfs(i, gid)
        gid += 1
ans = [0]*N
done = [False]*N
gid = 0
def dfs2(i, gid):
    done[i] = True
    ans[i] = D[gid][gids[i]]
    for nex in G[i]:
        if done[nex]: continue
        dfs2(nex, gid)
for i in range(N):
    if not done[i]:
        dfs2(i, gid)
        gid += 1
print((*ans))

