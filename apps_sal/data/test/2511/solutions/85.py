import networkx as nx

def factorial(n, mod):
    fac = [0] * (n + 1)
    inv = [0] * (n + 1)
    fac[0], inv[0] = 1, 1
    for i in range(1, n + 1):
        fac[i] = fac[i-1] * i % mod
        inv[i] = inverse(fac[i], mod)
    return fac, inv

def inverse(a, mod):
    a %= mod # 除数が正なら正になる
    p = mod
    x, y = 0, 1
    while a > 0:
        n = p // a
        p, a = a, p % a, 
        x, y = y, x - n * y
    return x % mod # 除数が正なら正になる

mod = 1000000007

n, k = list(map(int, input().split()))
graph = nx.Graph()
graph.add_nodes_from(list(range(n)))
for _ in range(n-1):
    a, b = [int(x) - 1 for x in input().split()]
    graph.add_edge(a, b)
if nx.degree(graph)[0] + 1 > k:
    print((0))
    return

fac, inv = factorial(k, mod)
ans = fac[k] * inv[k - nx.degree(graph)[0] - 1] % mod # nx.degree(graph)[0]:グラフの頂点0から出ている枝の数
for parent, child in nx.dfs_edges(graph, 0): # nx.dfs_edges(graph, 0):グラフの頂点0からDFS
    m = nx.degree(graph)[child]
    if m + 1 > k:
        print((0))
        return
    ans = ans * fac[k-2] % mod * inv[k-1-m] % mod
print(ans)

