import sys


def dfs1(root, links):
    parent = [0] * n
    subtree_count = [{} for _ in range(n)]
    q = [(root, -1, 0)]  # 2番目:親  3番目:0=初, 1=全ての子巡回後
    while q:
        v, p, t = q.pop()
        if t == 0:
            parent[v] = p
            q.append((v, p, 1))
            for u in links[v]:
                if u == p:
                    continue
                q.append((u, v, 0))
        elif p != -1:
            subtree_count[p][v] = sum(subtree_count[v].values()) + 1
    return parent, subtree_count


def dfs2(root, parent, subtree_count, d2, d2s):
    ans = 0
    q = [(root, 0)]
    while q:
        v, pc = q.pop()

        if len(subtree_count[v]) == 0:
            continue

        p = parent[v]
        children, st_counts = list(map(list, list(zip(*list(subtree_count[v].items())))))
        children.append(p)
        st_counts.append(pc)
        cl = len(st_counts)
        ct = sum(st_counts)

        for u, stc in list(subtree_count[v].items()):
            q.append((u, ct - stc + 1))

        if cl == 1:
            continue

        tmp = 0
        for stc in st_counts:
            tmp = (tmp + d2s[ct - stc]) % MOD
        tmp = (tmp - d2s[ct] * (cl - 1)) % MOD
        ans = (ans + (1 - tmp) * d2) % MOD
    return ans


n = int(input())
links = [set() for _ in range(n)]
for line in sys.stdin:
    a, b = list(map(int, line.split()))
    a -= 1
    b -= 1
    links[a].add(b)
    links[b].add(a)
root = 0
MOD = 10 ** 9 + 7
d2 = 500000004  # 2^-1 mod 10**9+7
d2s = [1]
for i in range(n):
    d2s.append(d2s[-1] * d2 % MOD)
parent, subtree_count = dfs1(root, links)
# print(parent)
# print(subtree_count)
ans = dfs2(root, parent, subtree_count, d2, d2s)
print(ans)
