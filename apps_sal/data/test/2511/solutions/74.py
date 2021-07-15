import sys
sys.setrecursionlimit(10**6)

def iig(vn, en):
    res = [[] for _ in range(vn)]
    for _ in range(en):
        ai, bi = [int(x) - 1 for x in input().split()]
        res[ai].append(bi)
        res[bi].append(ai)
    return res

def sep_pc(graph, root=0):
    parent = [-1 for _ in range(n)]
    children = [None for _ in range(n)]
    def f(x, p):
        parent[x] = p
        children[x] = [y for y in graph[x] if y != p]
        for y in graph[x]:
            if y != p:
                f(y, x)
        return
    f(root, -1)
    return parent, children

def itree(n, root=0):
    return sep_pc(iig(n, n - 1), root)

mod = 10**9 + 7

fact_range = 10**5 + 3
facts = [1] * (fact_range + 1)
for i in range(0, fact_range):
    facts[i+1] = facts[i] * (i + 1) % mod

ifacts = [1] * (fact_range + 1)
ifacts[fact_range] = pow(facts[fact_range], mod - 2, mod)
for i in range(fact_range, 0, -1):
    ifacts[i-1] = ifacts[i] * i % mod

n, k = list(map(int, input().split()))
p, c = itree(n)
def dfs(i=0, cur=k, avail=k-1):
    sz = len(c[i])
    if avail <= 0 and sz > 0 or sz > avail:
        return 0
    cur = cur * facts[avail] * ifacts[avail - sz] % mod
    for u in c[i]:
        cur = dfs(u, cur, k - 2)
    return cur
print((dfs()))

