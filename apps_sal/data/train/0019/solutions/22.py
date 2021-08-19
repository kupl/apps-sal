3


def main():
    t = int(input())
    for _ in range(t):
        (n1, k, d) = [int(e) for e in input().split()]
        a = [int(e) for e in input().split()]
        s = dict()
        for e in a[:d]:
            s[e] = s.get(e, 0) + 1
        b = len(s)
        n = b
        for i in range(d, n1):
            ai = a[i]
            aid = a[i - d]
            s[ai] = s.get(ai, 0) + 1
            if s[ai] == 1:
                n += 1
            s[aid] -= 1
            if s[aid] == 0:
                n -= 1
            b = min(n, b)
        print(b)


def __starting_point():
    main()


__starting_point()
