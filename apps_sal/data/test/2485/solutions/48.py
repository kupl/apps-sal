import sys
from collections import Counter


def main():
    H, W, M = map(int, sys.stdin.readline().rstrip().split())
    Mh = [0] * H
    Mw = [0] * W
    B = []
    for i in range(M):
        h, w = map(int, sys.stdin.readline().rstrip().split())
        Mh[h - 1] += 1
        Mw[w - 1] += 1
        B.append((h - 1, w - 1))

    nh = max(Mh)
    nw = max(Mw)

    lh = Counter(Mh)[nh]
    lw = Counter(Mw)[nw]

    out = 0
    for (h, w) in B:
        if Mh[h] == nh and Mw[w] == nw:
            out += 1

    if out == lh * lw:
        print(nh + nw - 1)
    else:
        print(nh + nw)


main()
