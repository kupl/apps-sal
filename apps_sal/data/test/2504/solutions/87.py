#dame datta...
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
def main():
    N, M, L = list(map(int, input().split()))
    l = [[0] * N for _ in range(N)]
    for _ in range(M):
        a, b, c = list(map(int, input().split()))
        if c > L:
            continue
        l[a-1][b-1] = c
        l[b-1][a-1] = c
    G = csr_matrix(l)
    d = floyd_warshall(G)
    l = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if d[i][j] <= L:
                l[i][j] = 1
    G = csr_matrix(l)
    d = floyd_warshall(G)
    Q = int(input())
    for _ in range(Q):
        s, t = list(map(int, input().split()))
        s -= 1
        t -= 1
        x = d[s][t]
        if x != float('inf'):
            print((int(x)-1))
        else:
            print((-1))
main()

