import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, X: "List[int]", Y: "List[int]"):
    parities = {(Xi + Yi) % 2 for Xi, Yi in zip(X, Y)}
    if len(parities) > 1:
        print((-1))
        return

    d = [1 << i for i in range(39)]
    if next(iter(parities)) == 0:
        d.append(1)

    print((len(d)))
    print((*d))

    x0 = -sum(d)
    for Xi, Yi in zip(X, Y):
        u = (Xi - x0 - Yi) // 2
        v = (Xi - x0 + Yi) // 2
        modes = []
        for i in range(39):
            ui = (u & (1 << i)) != 0
            vi = (v & (1 << i)) != 0
            modes.append({
                (False, False): "L",
                (False, True): "U",
                (True, False): "D",
                (True, True): "R",
            }[ui, vi])
        if len(d) > len(modes):
            modes.append("L")
        print(("".join(modes)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    X = [int()] * (N)
    Y = [int()] * (N)
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, X, Y)


def __starting_point():
    main()


__starting_point()
