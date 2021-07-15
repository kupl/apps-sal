def main():
    n, m = map(int, input().split())
    w = [c == '*' for i in range(n) for c in input()]
    nm = n * m
    q = [*[range(i, i + m) for i in range(0, nm, m)],
            *[range(i, nm, m) for i in range(m)]]
    e = [1000] * nm
    for f in True, False:
        for r in q:
            v = 0
            for i in r:
                if w[i]:
                    v += 1
                    if e[i] > v:
                        e[i] = v
                else:
                    v = e[i] = 0
        if f:
            w.reverse()
            e.reverse()
    e = [c if c != 1 else 0 for c in e]
    for f in True, False:
        for r in q:
            v = 0
            for i in r:
                if v > e[i]:
                    v -= 1
                else:
                    v = e[i]
                if v:
                    w[i] = False
        if f:
            w.reverse()
            e.reverse()
    if any(w):
        print(-1)
    else:
        r = []
        for i, c in enumerate(e):
            if c:
                r.append(f'{i//m+1} {i%m+1} {c-1}')
        print(len(r), '\n'.join(r), sep='\n')


main()
