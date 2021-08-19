from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
MOD = 1000000007
N = int(input())
childs = [[] for i in range(N + 1)]
for i in range(N - 1):
    (a, b) = list(map(int, input().split()))
    childs[a].append(b)
    childs[b].append(a)
dp = [0] * (N + 1)
tree_size = [0] * (N + 1)
ans = [0] * (N + 1)
n_inv = [1, 1]
n_j_mod = [1, 1]
for i in range(2, N + 1):
    n_inv.append(pow(i, MOD - 2, MOD) * n_inv[-1] % MOD)
    n_j_mod.append(n_j_mod[-1] * i % MOD)


def dfs(i, father=-1):
    method_num = 1
    t_size = 1
    for child in childs[i]:
        if child != father:
            (num, size) = dfs(child, i)
            method_num = method_num * num * n_inv[size] % MOD
            t_size += size
    method_num = method_num * n_j_mod[t_size - 1] % MOD
    dp[i] = method_num
    tree_size[i] = t_size
    return (method_num, t_size)


def rdfs(i, f_num, father=-1):
    ans[i] = dp[i] * f_num * n_j_mod[N - 1] * n_inv[N - tree_size[i]] * n_inv[tree_size[i] - 1] % MOD
    for child in childs[i]:
        if child != father:
            cf_num = ans[i] * n_j_mod[tree_size[child]] * n_j_mod[N - tree_size[child] - 1] * n_inv[N - 1] * pow(dp[child], MOD - 2, MOD) % MOD
            rdfs(child, cf_num, i)


dfs(1)
rdfs(1, 1)
print('\n'.join(list(map(str, ans[1:]))))
