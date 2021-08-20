from itertools import product
import sys
try:
    from typing import List, Tuple
except ImportError:
    pass
MOD = 1000000007


def isvalid(ptn: 'Tuple[bool]'):
    return not any((h1 and h2 for (h1, h2) in zip(ptn, ptn[1:])))


def solve(H: int, W: int, K: int):
    validptns = [ptn for ptn in product((False, True), repeat=W - 1) if isvalid(ptn)]
    dp = [1 if i == K - 1 else 0 for i in range(W)]
    for _ in range(H):
        newdp = [0] * W
        for ptn in validptns:
            for s in range(W):
                t = s
                if s < W - 1 and ptn[s]:
                    t = s + 1
                elif s > 0 and ptn[s - 1]:
                    t = s - 1
                newdp[t] += dp[s]
                newdp[t] %= MOD
        dp = newdp
    print(dp[0])


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))
    W = int(next(tokens))
    K = int(next(tokens))
    solve(H, W, K)


def __starting_point():
    main()


__starting_point()
