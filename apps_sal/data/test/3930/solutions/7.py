import sys
from itertools import accumulate
from collections import Counter

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def solve():
    n, k = map(int, input().split())
    A = [int(i) for i in input().split()]
    cs = [0] + list(accumulate(A))
    S = Counter()
    ans = 0

    if k == 1:
        for i in range(n, -1, -1):
            if i == n:
                S[cs[i]] += 1
                continue

            if cs[i] + 1 in S:
                ans += S[cs[i] + 1]

            S[cs[i]] += 1
    elif k == -1:
        for i in range(n, -1, -1):
            if i == n:
                S[cs[i]] += 1
                continue

            if cs[i] + 1 in S:
                ans += S[cs[i] + 1]
            if cs[i] - 1 in S:
                ans += S[cs[i] - 1]

            S[cs[i]] += 1
    else:
        for i in range(n, -1, -1):
            if i == n:
                S[cs[i]] += 1
                continue

            w = 1
            while abs(w) < 10**14 + 1:
                if cs[i] + w in S:
                    ans += S[cs[i] + w]
                w *= k

            S[cs[i]] += 1
    print(ans)


def __starting_point():
    solve()
__starting_point()
