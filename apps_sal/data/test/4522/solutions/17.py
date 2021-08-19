def find_ancestor(i, father):
    if father[i] == i:
        return i
    father[i] = find_ancestor(father[i], father)
    return father[i]


def connect(i, j, father, n_child):
    i_anc = find_ancestor(i, father)
    j_anc = find_ancestor(j, father)
    if n_child[i_anc] > n_child[j_anc]:
        n_child[i_anc] += n_child[j_anc]
        father[j_anc] = i_anc
    else:
        n_child[j_anc] += n_child[i_anc]
        father[i_anc] = j_anc


(n, m) = list(map(int, input().split()))
edges = []
father = [i for i in range(n)]
n_child = [1] * n
for i in range(n - 1):
    (i, j, w) = list(map(int, input().split()))
    edges.append((i - 1, j - 1, w))
edges.sort(key=lambda x: -x[2])
queries = list(map(int, input().split()))
s_queries = sorted(queries)
ans = {}
w_limit = []
ans_cum = 0
for query in s_queries:
    while len(edges) and edges[-1][2] <= query:
        (i, j, w) = edges[-1]
        edges.pop()
        i_anc = find_ancestor(i, father)
        j_anc = find_ancestor(j, father)
        ans_cum += n_child[i_anc] * n_child[j_anc]
        connect(i, j, father, n_child)
    ans[query] = ans_cum
print(' '.join(list(map(str, [ans[query] for query in queries]))))
