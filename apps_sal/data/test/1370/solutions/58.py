def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    (h, w, k) = map(int, input().split())
    field = [[] for i in range(h)]
    for i in range(h):
        field[i] = [int(s) for s in input()]
    import numpy as np
    field = np.array(field, dtype=int)
    inf = 10 ** 4
    ans = inf
    for i in range(2 ** (h - 1)):
        prev = 0
        damy = []
        tmp_ans = format(i, 'b').count('1')
        for j in range(h - 1):
            if i >> j & 1:
                damy.append(field[prev:j + 1].sum(axis=0))
                prev = j + 1
        damy.append(field[prev:].sum(axis=0))
        damy = np.array(damy, dtype=int).T
        if (damy > k).any():
            continue
        prev = 0
        cnt_w = np.zeros(tmp_ans + 1, dtype=int)
        for l in range(w):
            cnt_w += damy[l]
            if (cnt_w > k).any():
                cnt_w = damy[l]
                tmp_ans += 1
        ans = min(ans, tmp_ans)
    print(ans)


def __starting_point():
    main()


__starting_point()
