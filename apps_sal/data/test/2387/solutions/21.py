import sys


def parse(s):
    bottom = 0
    delta = 0
    for c in s:
        delta += (1 if c == "(" else -1)
        bottom = min(bottom, delta)
    return bottom, delta


def compute(pars):
    pars.sort(reverse=True)
    h = 0
    for bottom, delta in pars:
        if h + bottom < 0:
            print("No")
            return
        h += delta
    return h


def main():
    N = int(input())

    incs = []
    decs = []
    for _ in range(N):
        bottom, delta = parse(input())
        if delta > 0:
            incs.append((bottom, delta))
        else:
            decs.append((bottom - delta, -delta))

    inc_tot = compute(incs)
    dec_tot = compute(decs)
    if inc_tot == dec_tot:
        print("Yes")
    else:
        print("No")


def __starting_point():
    main()


__starting_point()
