from collections import Counter, defaultdict
from itertools import product
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(H: int, W: int, N: int, a: "List[int]", b: "List[int]"):
    d = defaultdict(int)
    for ai, bi in zip(a, b):
        for da, db in product((-1, 0, 1), repeat=2):
            aj = ai - 1 + da
            bj = bi - 1 + db
            if 1 <= aj <= H - 2 and 1 <= bj <= W - 2:
                d[aj, bj] += 1
    c = Counter(list(d.values()))
    e = [c[i] for i in range(1, 10)]
    print(((H - 2) * (W - 2) - sum(e)))
    for ei in e:
        print(ei)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))
    W = int(next(tokens))
    N = int(next(tokens))
    a = [int()] * (N)
    b = [int()] * (N)
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(H, W, N, a, b)


def __starting_point():
    main()


__starting_point()
