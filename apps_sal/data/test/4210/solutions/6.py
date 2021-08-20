def main():
    (n, k) = list(map(int, input().split()))
    (aa, cn1, cn2, sz, res) = ([], {}, {}, {}, 0)
    for w in input().split():
        a = int(w)
        if a in cn1:
            cn1[a] += 1
        else:
            cn1[a] = 1
            sz[a] = len(w)
    for (a, v) in list(cn1.items()):
        t = (sz[a], a % k)
        cn2[t] = cn2.get(t, 0) + v
    scale1 = [10 ** i + 1 for i in range(11)]
    scale2 = [1 - s for s in scale1]
    for (a, v) in list(cn1.items()):
        for s in range(1, 11):
            x = a * scale2[s] % k
            res += cn2.get((s, x), 0) * v
        if not a * scale1[sz[a]] % k:
            res -= v
    print(res)


def __starting_point():
    main()


__starting_point()
