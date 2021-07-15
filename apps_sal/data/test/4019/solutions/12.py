import os
from io import BytesIO
input = BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    def union(u, v):
        p, q = find(u), find(v)
        if p == q: return
        if rank[p] < rank[q]: p, q = q, p
        if rank[p] == rank[q]: rank[p] += 1
        parent[q] = p

    def find(u):
        p = parent[u]
        if p == u: return u
        root = find(p)
        parent[u] = root
        return root


    n, m, D = map(int, input().split())
    E = []
    E0 = []
    E0rmn = []
    MSTE = []

    parent = list(range(n))
    rank = [0] * n

    for _ in range(m):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        if u == 0 or v == 0:
            E0.append((u, v))
        else:
            E.append((u, v))

    if len(E0) < D:
        print('NO')
        return

    for u, v in E:
        if find(u) != find(v):
            union(u, v)
            MSTE.append((u, v))

    k = 0
    for u, v in E0:
        if find(u) != find(v):
            union(u, v)
            MSTE.append((u, v))
            k += 1
        else:
            E0rmn.append((u, v))

    if D < k:
        print('NO')
        return

    while k < D:
        e = E0rmn.pop()
        MSTE.append(e)
        k += 1

    parent = list(range(n))
    rank = [0] * n

    out = ['YES']
    for u, v in reversed(MSTE):
        if find(u) != find(v):
            union(u, v)
            out.append(str(u+1) + ' ' + str(v+1))

    print('\n'.join(out))

main()
