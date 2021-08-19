from itertools import accumulate


def bs(ws, w):
    (i, e) = (-1, len(ws) - 1)
    while e - i > 1:
        m = (e + i) // 2
        if w <= ws[m]:
            e = m
        else:
            i = m
    return e


input()
worms = list(accumulate(map(int, input().split())))
input()
tofind = list(map(int, input().split()))
print('\n'.join((str(bs(worms, w) + 1) for w in tofind)))
