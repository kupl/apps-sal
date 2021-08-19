from collections import Counter, defaultdict
import sys
input = sys.stdin.readline


def read():
    (H, W, M) = list(map(int, input().strip().split()))
    HW = []
    for i in range(M):
        (h, w) = list(map(int, input().strip().split()))
        HW.append((h, w))
    return (H, W, M, HW)


def solve(H, W, M, HW):
    hcount = Counter()
    wcount = Counter()
    for (h, w) in HW:
        hcount[h] += 1
        wcount[w] += 1
    hm = hcount.most_common()
    wm = wcount.most_common()
    hmax = hm[0][1]
    wmax = wm[0][1]
    hn = len([1 for (k, v) in list(hcount.items()) if v == hmax])
    wn = len([1 for (k, v) in list(wcount.items()) if v == wmax])
    m = hn * wn
    for (h, w) in HW:
        if hcount[h] == hmax and wcount[w] == wmax:
            m -= 1
    if m == 0:
        return hmax + wmax - 1
    return hmax + wmax


def __starting_point():
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print('%s' % str(outputs))


__starting_point()
