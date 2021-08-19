import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
from itertools import permutations
I = np.array(sys.stdin.read().split(), dtype=np.int64)
(n, m, R) = I[:3]
r = I[3:3 + R] - 1
(a, b, c) = I[3 + R:].reshape(-1, 3).T
graph = csr_matrix((c, (a - 1, b - 1)), shape=(n, n))


def main():
    dist = floyd_warshall(graph, directed=False).astype(np.int64)
    perms = np.array(list(permutations(r)))
    res = dist[perms[:, :-1], perms[:, 1:]]
    ans = np.amin(np.sum(res, axis=1))
    return ans


def __starting_point():
    ans = main()
    print(ans)


__starting_point()
