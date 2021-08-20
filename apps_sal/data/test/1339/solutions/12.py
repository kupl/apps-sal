def main():
    n = int(input())
    (l, r) = ([], [])
    for _ in range(n):
        (a, b) = map(int, input().split())
        l.append(a)
        r.append(b)
    l.append(min(l))
    r.append(max(r))
    l = list(zip(l, r))
    idx = l.index(l[-1])
    print(-1 if idx == n else idx + 1)


def __starting_point():
    main()


__starting_point()
