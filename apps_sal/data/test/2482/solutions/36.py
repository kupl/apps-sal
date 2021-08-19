from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, K, L = list(map(int, input().split()))

# Group1
G1 = [[] for i in range(N)]
for i in range(K):
    p, q = list(map(int, input().split()))
    p -= 1
    q -= 1
    G1[p].append(q)
    G1[q].append(p)
gids = [0] * N
done = [False] * N


def dfs1(i, gid):
    gids[i] = gid
    done[i] = True
    for nex in G1[i]:
        if done[nex]:
            continue
        dfs1(nex, gid)


gid = 0
for i in range(N):
    if not done[i]:
        dfs1(i, gid)
        gid += 1

# Group2
G = [[] for i in range(N)]
for i in range(L):
    r, s = list(map(int, input().split()))
    r -= 1
    s -= 1
    G[r].append(s)
    G[s].append(r)
done = [False] * N
D = []
gids2 = [0] * N


def dfs(i, gid):
    D[gid][gids[i]] += 1
    done[i] = True
    gids2[i] = gid
    for nex in G[i]:
        if done[nex]:
            continue
        dfs(nex, gid)


gid = 0
for i in range(N):
    if not done[i]:
        D.append(defaultdict(int))
        dfs(i, gid)
        gid += 1

# answer
ans = [0] * N
for i in range(N):
    ans[i] = D[gids2[i]][gids[i]]
print((*ans))
