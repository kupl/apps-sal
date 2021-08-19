# D - Even Relation
from typing import List, Tuple


def main():
    N, *X = list(map(int, open(0).read().split()))
    tree: List[List[Tuple[int, int]]] = [[] for _ in range(N + 1)]
    for u, v, w in zip(*[iter(X)] * 3):
        w %= 2
        tree[u].append((v, w)), tree[v].append((u, w))

    color = [-1] * (N + 1)
    color[1] = 1
    stack = [1]
    while stack:
        u = stack.pop()
        cur = color[u]
        for v, w in tree[u]:
            if color[v] != -1:
                continue
            color[v] = cur ^ w
            stack.append(v)

    print(("\n".join(map(str, color[1:]))))


def __starting_point():
    main()


__starting_point()
