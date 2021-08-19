from scipy.sparse.csgraph import connected_components, bellman_ford, NegativeCycleError
from scipy.sparse import csr_matrix

N, M = list(map(int, input().split()))
frm, to, length = [], [], []
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    frm.append(a - 1)
    to.append(b - 1)
    length.append(-c)

# N-1→0の辺を追加してから卿連結判定⇒ゴールにたどり着けない閉路を除外
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
    print(ans)
except NegativeCycleError:
    print('inf')
