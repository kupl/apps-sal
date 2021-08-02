from itertools import chain


def main(n, a, info=False):
    winner = a[-1]
    looser = 3 - winner
    csw, csl, pw, pl, ans = [0], [0], [-1], [-1], []
    nw, nl = a.count(winner), a.count(looser)
    for i in range(n):
        if a[i] == winner: pw.append(i)
        else: pl.append(i)
        csw.append(csw[-1] + int(a[i] == winner))
        csl.append(csl[-1] + int(a[i] == looser))
    pw += [n * 10] * n
    pl += [n * 10] * n
    csw += [0] * n
    csl += [0] * n
    if info:
        print("a: ", a)
        print("csw: ", csw)
        print("csl: ", csl)
        print("pw: ", pw)
        print("pl: ", pl)
    for t in chain(list(range(1, nw // 2 + 1)), [nw]):
        s = l = i = 0
        sw = sl = 0
        while i < n:
            xw = pw[csw[i] + t]
            xl = pl[csl[i] + t]
            if xw < xl: s += 1
            else: l += 1
            i = min(xw, xl) + 1
            if info:
                print(s, t, ": ", t, i, s, l, xw, xl)
        if s > l and i <= n and csw[i] == nw:
            ans.append((s, t))
    print(len(ans))
    for x, y in sorted(ans):
        print(x, y)


def main_input():
    n = int(input())
    a = [int(i) for i in input().split()]
    main(n, a)


def __starting_point():
    main_input()


__starting_point()
