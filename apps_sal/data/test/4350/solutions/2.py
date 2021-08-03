def main():
    n, m = map(int, input().split())
    ll = [c == '*' for _ in range(n) for c in input()]
    nm = n * m
    RLUD = [*[range(i, i + m) for i in range(0, nm, m)],
            *[range(i, nm, m) for i in range(m)]]
    cc = [1000] * nm
    for f in True, False:
        for r in RLUD:
            v = 0
            for i in r:
                if ll[i]:
                    v += 1
                    if cc[i] > v:
                        cc[i] = v
                else:
                    v = cc[i] = 0
        if f:
            ll.reverse()
            cc.reverse()
    cc = [c if c != 1 else 0 for c in cc]
    for f in True, False:
        for r in RLUD:
            v = 0
            for i in r:
                if v > cc[i]:
                    v -= 1
                else:
                    v = cc[i]
                if v:
                    ll[i] = False
        if f:
            ll.reverse()
            cc.reverse()
    if any(ll):
        print(-1)
    else:
        res = []
        for i, c in enumerate(cc):
            if c:
                res.append(f'{i//m+1} {i%m+1} {c-1}')
        print(len(res), '\n'.join(res), sep='\n')


def __starting_point():
    main()


__starting_point()
