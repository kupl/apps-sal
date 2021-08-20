from bisect import bisect_left
(n, m, k) = map(int, input().split(' '))
holes = list(map(int, input().split(' ')))
curr = 1
found = False
holes = sorted(holes)
H = len(holes)


def bins(x, bot, top=None):
    top = top if top is not None else H
    pos = bisect_left(holes, x, bot, top)
    return pos != top and holes[pos] == x


if curr in holes:
    print(curr)
    found = True
else:
    for a0 in range(k):
        (u, v) = map(int, input().split(' '))
        if u == curr:
            curr = v
            if bins(curr, 0):
                print(curr)
                found = True
                break
        elif v == curr:
            curr = u
            if bins(curr, 0):
                print(curr)
                found = True
                break
if not found:
    print(curr)
