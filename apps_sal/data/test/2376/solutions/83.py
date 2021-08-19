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

    def rec(i, vec):
        if i == 4:
            ans = 0
            w_total = 0
            for j in range(4):
                w_total += (w_min + j) * vec[j]
            if w_total > W:
                return -1
            for j in range(4):
                ans += csums[j][vec[j]]
            return ans
        ans = 0
        for j in range(len(csums[i])):
            vec.append(j)
            ans = max(ans, rec(i + 1, vec))
            vec.pop()
        return ans
    print(rec(0, []))
    return


def __starting_point():
    main()


__starting_point()
