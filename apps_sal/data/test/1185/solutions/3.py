def main():
    (n, m, k) = list(map(int, input().split()))
    if m == 1:
        print(sum(sorted(map(int, input().split()), reverse=True)[:k]))
        return
    (l, x) = ([0], 0)
    for p in map(int, input().split()):
        x += p
        l.append(x)
    l = [b - a for (a, b) in zip(l, l[m:])]
    nxt = [0] * len(l)
    for start in range(0, k * m, m):
        (cur, nxt, x) = (nxt, [], 0)
        for (s, p) in zip(cur, l[start:]):
            s += p
            if x < s:
                x = s
            nxt.append(x)
    print(nxt[-1])


def __starting_point():
    main()


__starting_point()
