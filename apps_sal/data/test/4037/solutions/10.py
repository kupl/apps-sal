from functools import cmp_to_key
from operator import itemgetter


def main():
    n, r = list(map(int, input().split()))
    ps = [tuple(map(int, input().split())) for _ in range(n)]

    pos_ps = [(a, b) for a, b in ps if b >= 0]
    neg_ps = [(a, b) for a, b in ps if b < 0]

    def cmp(a, b):
        (aa, ab), (ba, bb) = a, b
        return max(aa, max(*b) - ab) - max(ba, max(*a) - bb)

    pos_ps.sort(key=itemgetter(0))
    neg_ps.sort(key=cmp_to_key(cmp))
    del cmp

    res = 0
    for a, b in pos_ps:
        if r >= a:
            res += 1
            r += b

    cur = [r]
    for a, b in neg_ps:
        nxt = [-1]*(len(cur)+1)
        for i, r in enumerate(cur):
            if r >= 0:
                nxt[i] = max(nxt[i], r)
                if r >= a:
                    nxt[i+1] = r + b
        while nxt[-1] < 0:
            nxt.pop()
        cur = nxt

    print(res + len(cur) - 1)


def __starting_point():
    main()

__starting_point()
