import itertools
import numpy as np
from scipy.sparse.csgraph import floyd_warshall


def main():
    N = int(input())
    matr = np.array([tuple(map(int, input().split())) for _ in range(N)], dtype=np.int64)
    way = floyd_warshall(matr).astype(int)
    if np.any(way < matr):
        print((-1))
        return

    ans = 0
    for a, b in itertools.combinations(list(range(N)), 2):
        eq = (matr[a, b] == (matr[a] + matr[:, b]))
        eq[a] = eq[b] = False
        if not np.any(eq):
            ans += matr[a, b]
    print(ans)


def __starting_point():
    main()

__starting_point()
