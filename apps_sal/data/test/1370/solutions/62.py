
def main():
    def calc(group):
        ret = max(group)
        ctr = [0] * H
        for c in range(W):
            need_cut = False
            for r, g in enumerate(group):
                ctr[g] += s[r][c]
                if ctr[g] > K:
                    need_cut = True
                    break

            if need_cut:
                ctr = [0] * H
                ret += 1
                for r, g in enumerate(group):
                    ctr[g] += s[r][c]
                    if ctr[g] > K:
                        return H * W
                continue
        return ret

    def gen():
        from itertools import accumulate, product

        for prod in product(list(range(2)), repeat=H - 1):
            group = [0]
            group.extend(accumulate(prod))
            yield calc(group)

    H, W, K = list(map(int, input().split()))
    s = []
    for _ in range(H):
        *row, = list(map(int, input()))
        s.append(row)

    ret = min(gen())
    print(ret)


def __starting_point():
    main()


__starting_point()
