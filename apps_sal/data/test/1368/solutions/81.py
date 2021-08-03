#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def comb(n: int, r: int):
    if r > n - r:
        return comb(n, n - r)
    p = q = 1
    for i in range(r):
        p *= n - i
        q *= i + 1
    return p // q


def solve(N: int, A: int, B: int, v: "List[int]"):
    v.sort(reverse=True)
    sl = v[:A]
    print((sum(sl) / A))
    if len(set(sl)) == 1:
        m = sl[0]
        cm = v.count(m)
        ans = 0
        for z in range(A, min(cm, B) + 1):
            ans += comb(cm, z)
        print(ans)
    else:
        m = sl[-1]
        cm = v.count(m)
        print((comb(cm, sl.count(m))))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    v = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, v)


def __starting_point():
    main()


__starting_point()
