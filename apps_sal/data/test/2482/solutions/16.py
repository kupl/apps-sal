import numpy as np
from collections import Counter
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix


def int1(x): return int(x) - 1


N, K, L = map(int, input().split())
roads = np.array([tuple(map(int1, input().split())) for _ in range(K)]).T
railways = np.array([tuple(map(int1, input().split())) for _ in range(L)]).T


def connected(G, M):
    matr = csr_matrix((np.ones(M, dtype=int), G), shape=(N, N))
    _, labels = connected_components(matr)
    return labels


roads_connection = connected(roads, K).tolist()
railways_connection = connected(railways, L).tolist()

ct = Counter((roads_connection[i], railways_connection[i]) for i in range(N))
ans = [ct[(roads_connection[i], railways_connection[i])] for i in range(N)]
print(*ans)
