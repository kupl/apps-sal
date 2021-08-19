from collections import defaultdict
from operator import itemgetter


def solve(N, X, D):
    if D < 0:
        D = -D
        X = -X
    elif D == 0:
        if X == 0:
            return 1
        return N + 1
    s = defaultdict(list)
    for k in range(N + 1):
        p = k * X % D
        q = k * X // D
        a = k * (k - 1) // 2
        b = (N - 1) * k - a + 1
        s[p].append((a + q, b + q))
    ans = 0
    for v in list(s.values()):
        if not v:
            continue
        v.sort()
        (a, b) = v[0]
        for (x, y) in v[1:]:
            if b < x:
                ans += b - a
                (a, b) = (x, y)
            else:
                b = max(b, y)
        ans += b - a
    return ans


def __starting_point():
    (N, X, D) = list(map(int, input().split()))
    print(solve(N, X, D))


__starting_point()
