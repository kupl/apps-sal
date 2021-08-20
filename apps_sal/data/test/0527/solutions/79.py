def abc138_e():
    s = str(input())
    t = str(input())
    sd = dict()
    for (i, c) in enumerate(s):
        if sd.get(c) == None:
            sd[c] = []
        sd[c].append(i)
    from bisect import bisect_left
    k = 0
    p = 0
    for c in t:
        if sd.get(c) == None:
            return print(-1)
        idx = bisect_left(sd[c], p)
        if idx == len(sd[c]):
            k += 1
            p = 0
            idx = bisect_left(sd[c], p)
        p = sd[c][idx] + 1
    ans = k * len(s) + p
    return print(ans)


def __starting_point():
    abc138_e()


__starting_point()
