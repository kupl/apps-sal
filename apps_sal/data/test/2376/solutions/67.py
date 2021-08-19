from collections import defaultdict


def main():
    N, W = list(map(int, input().split(' ')))
    items, cumsums = defaultdict(list), defaultdict(list)
    w_0 = 0
    for i in range(N):
        w, v = list(map(int, input().split(' ')))
        if i == 0:
            w_0 = w
        items[w].append(v)
    for w in items.keys():
        items[w].sort(reverse=True)
        cumsum_w, cumsum_v = 0, 0
        for v in items[w]:
            cumsum_w += w
            cumsum_v += v
            # w - w_0 is in [0, 1, 2, 3]
            cumsums[w - w_0].append((cumsum_w, cumsum_v))

    def dfs(cur, rest_w):
        if cur == 0:
            max_v = 0
            for cumsum_w, cumsum_v in cumsums[cur]:
                if cumsum_w <= rest_w:
                    max_v = cumsum_v
            return max_v
        else:
            ret = dfs(cur - 1, rest_w)
            for cumsum_w, cumsum_v in cumsums[cur]:
                if rest_w >= cumsum_w:
                    ret = max([ret, cumsum_v + dfs(cur - 1, rest_w - cumsum_w)])
            return ret

    print(dfs(3, W))


def __starting_point():
    main()


__starting_point()
