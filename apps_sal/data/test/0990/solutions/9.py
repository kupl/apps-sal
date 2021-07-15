#!/usr/bin/env python3
import sys
input = sys.stdin.readline
 
n = int(input())
edge = [[] for _ in range(n)]
edge_dict = dict()
 
for i in range(n - 1):
    a, b = [int(item) - 1 for item in input().split()]
    edge[a].append(b)
    edge[b].append(a)
    if a > b:
        edge_dict[(b, a)] = i
    else:
        edge_dict[(a, b)] = i
 
m = int(input())
uv = []
for _ in range(m):
    uv.append([int(item) - 1 for item in input().split()])
 
def dfs(p, v, dest):
    if v == dest:
        return [v]
    if p != -1 and len(edge[v]) == 1:
        return False
    for nv in edge[v]:
        if nv == p:
            continue
        ret = dfs(v, nv, dest)
        if ret:
            return ret + [v]
    return False
 
# edge-bitset of each set of constraints
edgest = [0] * 2**m
for i, (u, v) in enumerate(uv):
    ret = dfs(-1, u, v)
    for uu, vv in zip(ret, ret[1:]):
        if uu > vv:
            uu, vv = vv, uu
        if (uu, vv) in edge_dict:
            edgest[1 << i] |= (1 << edge_dict[(uu, vv)])
for i in range(1, 2**m):
    lsb = i & (-i)
    edgest[i] = edgest[i ^ lsb] | edgest[lsb]
 
# dp[set of constraints]
dp = [0] * 2**m
dp[0] = 1 << (n - 1)
ans = dp[0]
for i in range(1, 2**m):
    lsb = i & (-i)
    limit_num = bin(edgest[i] ^ edgest[i ^ lsb]).count("1")
    dp[i] = dp[i ^ lsb] >> limit_num
    # Inclusion and exclusion
    if bin(i).count("1") % 2 == 0:
        ans += dp[i]
    else:
        ans -= dp[i]
print(ans)
