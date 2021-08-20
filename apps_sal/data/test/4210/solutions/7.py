def main():
    (n, k) = map(int, input().split())
    (aa, cnt, res) = ([], {}, 0)
    scale = [10 ** i + 1 for i in range(11)]
    for w in input().split():
        (a, s) = (int(w), len(w))
        aa.append(a)
        if not a * scale[s] % k:
            res -= 1
        t = (s, a % k)
        cnt[t] = cnt.get(t, 0) + 1
    scale = [1 - i for i in scale]
    for a in aa:
        for s in range(1, 11):
            x = a * scale[s] % k
            res += cnt.get((s, x), 0)
    print(res)


def __starting_point():
    main()


__starting_point()
