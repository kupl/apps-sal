
def foo(x: int):
    if x <= 0: return 0
    a = len(str(x))
    ret = a * (x * x + x) // 2

    t = 1
    cur, prv = 10, 1
    while t < a:
        l = a - t

        freq = cur - prv
        ret -= l * (freq * ((x - prv + 1) + (x - (cur - 1) + 1)) // 2)

        cur, prv = 10 * cur, 10 * prv
        t += 1

    return ret


def bar(x: int):
    if x <= 0: return 0
    a = len(str(x))
    ret = a * x

    t = 1
    cur, prv = 10, 1
    while t < a:
        l = a - t

        freq = cur - prv
        ret -= l * freq

        cur, prv = 10 * cur, 10 * prv
        t += 1

    return ret


def solve(k):
    lo, hi = 0, k
    while lo < hi:
        mid = (lo + 1 + hi) >> 1
        L = foo(mid)
        lo, hi = (mid, hi) if L < k else (lo, mid - 1)

    L = foo(lo)

    x, y = 0, lo + 1
    while x < y:
        mid = (x + 1 + y) >> 1
        T = bar(mid)
        x, y = (mid, y) if L + T < k else (x, mid - 1)

    T = bar(x)

    return str(x + 1)[(k - L - T) - 1]


q = int(input())
for test_case in range(q):
    k = int(input())
    print(solve(k))
