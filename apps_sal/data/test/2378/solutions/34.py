import sys
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7
N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    (A, B) = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)


def dfs(u, par):
    visited[u] = True
    ret = 1
    for v in tree[u]:
        if not visited[v]:
            ret += dfs(v, u)
    if par > 0:
        tree_dic[u, par] = ret
    return ret


visited = [False] * (N + 1)
tree_dic = {}
dfs(1, 0)
bumbo = pow(2, N, MOD)
bunshi = (pow(2, N, MOD) - 1 - N * pow(2, N - 1, MOD)) % MOD
for x in tree_dic.values():
    term = (pow(2, x, MOD) - 1) * (pow(2, N - x, MOD) - 1)
    bunshi += term
    bunshi %= MOD
answer = bunshi * pow(bumbo, MOD - 2, MOD)
answer %= MOD
print(answer)
