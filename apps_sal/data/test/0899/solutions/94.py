from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix


def main():
    N, M = list(map(int, input().split()))
    w = [[0] * N for i in range(N)]
    l = []
    for i in range(M):
        a, b, c = list(map(int, input().split()))
        a -= 1
        b -= 1
        w[a][b] = w[b][a] = c
        l.append((a, b, c))
    G = csr_matrix(w)
    d = floyd_warshall(G, directed=False)
    r = 0
    for a, b, c in l:
        if d[a][b] != c:
            r += 1
    return r


print((main()))
