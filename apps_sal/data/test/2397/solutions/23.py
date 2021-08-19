def __starting_point():
    (n, k) = map(int, input().split())
    aa = list(map(int, input().split()))
    ss = [0]
    for a in reversed(aa):
        ss.append(ss[-1] + a)
    ss = ss[1:]
    if k == 1:
        print(ss[-1])
        return
    print(ss[-1] + sum(sorted(ss[:-1])[-(k - 1):]))


__starting_point()
