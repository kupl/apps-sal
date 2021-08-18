from collections import Counter
N, K, L = list(map(int, input().split()))


def get_root(par, node):
    if par[node] == node:
        return node
    root = get_root(par, par[node])
    par[node] = root
    return root


def union(par, rank, a, b):
    root_a, root_b = get_root(par, a), get_root(par, b)
    if root_a == root_b:
        return
    rank_a, rank_b = rank[root_a], rank[root_b]
    if rank_a < rank_b:
        par[root_a] = root_b
    else:
        par[root_b] = root_a
        if rank_a == rank_b:
            rank[root_a] += 1


par1 = [i for i in range(N)]
rank1 = [1] * N
for _ in range(K):
    a, b = list(map(int, input().split()))
    union(par1, rank1, a - 1, b - 1)

par2 = [i for i in range(N)]
rank2 = [1] * N
for _ in range(L):
    a, b = list(map(int, input().split()))
    union(par2, rank2, a - 1, b - 1)

ct = Counter()
for i in range(N):
    a = get_root(par1, i)
    b = get_root(par2, i)
    ct[(a, b)] += 1

print((' '.join([str(ct[(par1[i], par2[i])]) for i in range(N)])))
