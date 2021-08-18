from collections import defaultdict
from scipy.sparse.csgraph import connected_components, bellman_ford, NegativeCycleError
from scipy.sparse import csr_matrix

N, M, P = list(map(int, input().split()))

d = defaultdict(lambda: P)
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    d[(a - 1, b - 1)] = min(d[(a - 1, b - 1)], P - c)

M = len(d)
frm, to, length = [], [], []
for (a, b), c in list(d.items()):
    frm.append(a)
    to.append(b)
    length.append(c)

connect_check = csr_matrix(([1] * (M + 1), (frm + [N - 1], to + [0])), shape=(N, N))
_, labels = connected_components(connect_check, connection='strong')
label_num = labels[0]
frm_c, to_c, length_c = [], [], []
for i in range(M):
    if labels[frm[i]] == labels[to[i]] == label_num:
        frm_c.append(frm[i])
        to_c.append(to[i])
        length_c.append(length[i])

matr = csr_matrix((length_c, (frm_c, to_c)), shape=(N, N))

try:
    ans = -int(bellman_ford(matr, indices=0)[N - 1])
    print((max(0, ans)))
except NegativeCycleError:
    print((-1))
