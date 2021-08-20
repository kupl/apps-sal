import sys
from collections import defaultdict
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline
ra = range
enu = enumerate


def mina(*argv, sub=1):
    return list([x - sub for x in argv])


def read_a_int():
    return int(read())


def read_ints():
    return list(map(int, read().split()))


MOD = 10 ** 9 + 7
(N, K) = read_ints()
tree = defaultdict(lambda: [])
for _ in range(N - 1):
    (a, b) = read_ints()
    (a, b) = mina(a, b)
    tree[a].append(b)
    tree[b].append(a)


def perm_mod(n, r, mod=MOD):
    if n < r:
        return 0
    ret = 1
    for _ in range(r):
        ret *= n
        ret %= mod
        n -= 1
    return ret


def dfs(u, p):
    if len(tree[u]) == 1 and tree[u][0] == p:
        return 1
    ret = 1
    for to in tree[u]:
        if to == p:
            continue
        ret *= dfs(to, u)
        ret %= MOD
    if p == -1:
        ret *= perm_mod(K, len(tree[u]) + 1)
    else:
        ret *= perm_mod(K - 2, len(tree[u]) - 1)
    return ret % MOD


print(dfs(0, -1))
