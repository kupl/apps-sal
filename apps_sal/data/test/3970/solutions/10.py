def main():
    (n, k) = map(int, input().split())
    if n == 1:
        print(1)
        return
    l = sorted(map(int, input().split()))
    baned = set()
    s = set(l)
    if k > 1:
        for p in l:
            if p not in baned:
                p *= k
                s.discard(p)
                baned.add(p)
    print(len(s))


def __starting_point():
    main()


__starting_point()
