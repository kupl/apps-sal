
def solve(ls, k, debug=0):
    modulo = 10 ** 9 + 7
    n = len(ls)
    n_neg = 0
    for i in range(n):
        n_neg += ls[i] < 0
    n_pos = n - n_neg

    ls_abs = [abs(x) for x in ls]
    ls_abs_argsort = sorted(list(range(n)), key=lambda i: -ls_abs[i])

    if n_neg >= k:
        positive = (k % 2 == 0) or (n_pos > 0)
    else:
        positive = (n_neg % 2 == 0) or (n > k)

    if not positive:
        p = 1
        for i in range(k):
            x = ls[ls_abs_argsort[-1 - i]]
            p *= x
            p %= modulo
        return p

    s = 1
    for i in range(k):
        x = ls[ls_abs_argsort[i]]
        s *= -1 if x < 0 else 1

    if s > 0:
        p = 1
        for i in range(k):
            x = ls[ls_abs_argsort[i]]
            p *= x
            p %= modulo
        return p

    opt1 = None
    opt2 = None
    neg1 = pos1 = None
    pos2 = neg2 = None

    swap_pos = None
    for i in range(k, n):
        if ls[ls_abs_argsort[i]] >= 0:
            swap_pos = i
            pos1 = ls[ls_abs_argsort[i]]
            break

    swap_neg = None
    for i in range(k)[::-1]:
        if ls[ls_abs_argsort[i]] < 0:
            swap_neg = i
            neg1 = ls[ls_abs_argsort[i]]
            break

    if swap_pos is not None and swap_neg is not None:
        p = 1
        p *= ls[ls_abs_argsort[swap_pos]]
        p %= modulo
        for i in range(k):
            if i == swap_neg:
                continue
            x = ls[ls_abs_argsort[i]]
            p *= x
            p %= modulo
        opt1 = p

    swap_pos = None
    for i in range(k)[::-1]:
        if ls[ls_abs_argsort[i]] >= 0:
            swap_pos = i
            pos2 = ls[ls_abs_argsort[i]]
            break

    swap_neg = None
    for i in range(k, n):
        if ls[ls_abs_argsort[i]] < 0:
            swap_neg = i
            neg2 = ls[ls_abs_argsort[i]]
            break

    if swap_pos is not None and swap_neg is not None:
        p = 1
        p *= ls[ls_abs_argsort[swap_neg]]
        p %= modulo
        for i in range(k):
            if i == swap_pos:
                continue
            x = ls[ls_abs_argsort[i]]
            p *= x
            p %= modulo
            opt2 = p

    if opt1 is None:
        return opt2

    if opt2 is None:
        return opt1

    if pos1 * pos2 > neg1 * neg2:
        return opt1

    return opt2


def main(istr, ostr):
    n, k = list(map(int, istr.readline().strip().split()))
    ls = list(map(int, istr.readline().strip().split()))
    result = solve(ls, k)
    print(result, file=ostr)


def __starting_point():
    import sys

    main(sys.stdin, sys.stdout)


__starting_point()
