from scipy.sparse import csr_matrix, lil_matrix
from scipy.sparse.csgraph import bellman_ford, NegativeCycleError


def main():
    N, M, P = list(map(int, input().split()))
    A, B, C = [0] * M, [0] * M, [0] * M
    v = [set() for _ in range(N)]
    u = [set() for _ in range(N)]
    for i in range(M):
        a, b, c = list(map(int, input().split()))
        A[i], B[i], C[i] = a - 1, b - 1, P - c
        u[a - 1].add(b - 1)
        v[b - 1].add(a - 1)
    vv = set()
    cur = set([N - 1])
    while cur:
        vv |= cur
        cur = set().union(*(v[c] for c in cur)) - vv
    uu = set()
    cur = set([0])
    while cur:
        uu |= cur
        cur = set().union(*(u[c] for c in cur)) - uu
    reachable = vv & uu
    l = {}
    for a, b, c in zip(A, B, C):
        if a in reachable and b in reachable:
            l[(a, b)] = min(c, l.get((a, b), 10 ** 9))
    AA, BB, CC = [], [], []
    for (a, b), c in list(l.items()):
        AA.append(a)
        BB.append(b)
        CC.append(c)
    mx = csr_matrix((CC, (AA, BB)), shape=(N, N))
    try:
        dm = bellman_ford(mx, indices=[0])
    except NegativeCycleError:
        return -1
    return max(0, -int(dm[0][N - 1]))


print((main()))
