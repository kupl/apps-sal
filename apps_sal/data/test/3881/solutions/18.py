def main():
    n, q = list(map(int, input().split()))
    d, nxt, f = {c: [] for c in "abcdef"}, {"a"}, ''.join
    for _ in range(q):
        a, b = input().split()
        d[b].append(a)
    for _ in range(n - 1):
        cur, nxt = nxt, set()
        for l in map(list, cur):
            for s in d[l[0]]:
                l[0] = s
                nxt.add(f(l))
    print(len(nxt))


def __starting_point():
    main()


__starting_point()
