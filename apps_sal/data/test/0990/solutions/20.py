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
 
# edge-bitset of each constraint
target_edge = [0] * m
for i, (u, v) in enumerate(uv):
    ret = dfs(-1, u, v)
    for uu, vv in zip(ret, ret[1:]):
        if uu > vv:
            uu, vv = vv, uu
        if (uu, vv) in edge_dict:
            target_edge[i] |= (1 << edge_dict[(uu, vv)])

# edge-bitset of each set of constraints
edgest = [0] * 2**m
for i in range(1, 2**m):
    lsb = i & (-i)
    edgest[i] = edgest[i ^ lsb] | target_edge[lsb.bit_length() - 1]
 
# dp[set of constraints]
dp = [0] * 2**m
dp[0] = 1 << (n - 1)
ans = dp[0]
for i in range(1, 2**m):
    lsb = i & (-i)
    n_edgest = edgest[i]
    p_edgest = edgest[i ^ lsb]
    limit_num = bin(n_edgest ^ p_edgest).count("1")
    dp[i] = dp[i ^ lsb] >> limit_num
    if bin(i).count("1") % 2 == 0:
        ans += dp[i]
    else:
        ans -= dp[i]
print(ans)
