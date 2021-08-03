def main():
    n, m, p = list(map(int, input().split()))
    xlat, l, s, ll, lr = [0] * n, [], input(), list(range(-1, n)), list(range(1, n + 2))
    p -= 1
    for i, c in enumerate(s):
        if c == '(':
            l.append(i)
        else:
            j = l.pop()
            xlat[i] = j
            xlat[j] = i
    for c in input():
        if c == 'D':
            if s[p] == '(':
                p = xlat[p]
            q = ll[xlat[p]]
            p = lr[p]
            ll[p], lr[q] = q, p
            if p == n:
                p = ll[p]
        else:
            p = (lr if c == 'R' else ll)[p]
    q = p
    while p != -1:
        l.append(s[p])
        p = ll[p]
    l.reverse()
    del l[-1]
    while q != n:
        l.append(s[q])
        q = lr[q]
    print(''.join(l))


def __starting_point():
    main()


__starting_point()
