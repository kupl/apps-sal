import sys
from itertools import accumulate
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (N, W, *WV) = list(map(int, read().split()))
    weight = WV[::2]
    value = WV[1::2]
    w_min = min(weight)
    items = [[] for _ in range(4)]
    for (w, v) in zip(weight, value):
        items[w - w_min].append(v)
    for i in range(4):
        items[i].sort(reverse=True)
    csums = [0] * 4
    for i in range(4):
        csums[i] = [0]
        csums[i].extend(accumulate(items[i]))

    def rec(i, w, v):
        if i == 4:
            if w <= W:
                return v
            else:
                return -1
        ans = 0
        for j in range(len(csums[i])):
            ans = max(ans, rec(i + 1, w + (w_min + i) * j, v + csums[i][j]))
        return ans
    print(rec(0, 0, 0))
    return


def __starting_point():
    main()


__starting_point()
