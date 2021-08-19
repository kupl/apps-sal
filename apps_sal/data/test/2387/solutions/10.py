import cython


def main():
    import sys
    readline = sys.stdin.readline
    N: cython.longlong
    N = int(readline())
    S = [readline().strip() for i in range(N)]
    D = []
    (L, R) = ([], [])
    for s in S:
        l: cython.longlong = 0
        r: cython.longlong = 0
        for c in s:
            if c == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1
            else:
                l += 1
        if l == 0 and r == 0:
            pass
        elif l == 0:
            R.append(r)
        elif r == 0:
            L.append(l)
        else:
            D.append((l, r))
    L: cython.longlong
    R: cython.longlong
    L = sum(L)
    R = sum(R)
    inc = []
    dec = []
    for (l, r) in D:
        if l > r:
            inc.append((l, r))
        else:
            dec.append((l, r))
    inc.sort(key=lambda x: x[1])
    dec.sort(key=lambda x: -x[1])
    D = inc + dec
    l: cython.longlong
    r: cython.longlong
    for (_, (l, r)) in enumerate(D):
        L -= r
        if L < 0:
            print('No')
            return
        L += l
    if L == R:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
