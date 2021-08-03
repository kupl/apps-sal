from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
from itertools import permutations


def main():
    N, M, R = list(map(int, input().split()))
    r = list(map(int, input().split()))
    r = [i - 1 for i in r]
    l = [[0] * N for _ in range(N)]
    for _ in range(M):
        a, b, c = list(map(int, input().split()))
        a -= 1
        b -= 1
        l[a][b] = c
        l[b][a] = c
    G = csr_matrix(l)
    dd = dijkstra(G, directed=False)
    ans = 10**100
    for i in permutations(r, len(r)):
        t = 0
        for j in range(len(r) - 1):
            t += dd[i[j]][i[j + 1]]
        ans = min(ans, t)
    return int(ans)


print((main()))
