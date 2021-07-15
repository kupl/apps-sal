def main():
    n, m, d = list(map(int, input().split()))
    l = [x for _ in range(n) for x in map(int, input().split())]
    n *= m
    m = min(l)
    for i, x in enumerate(l):
        x -= m
        if x % d:
            print(-1)
            return
        l[i] = x
    l.sort()
    m = l[n // 2]
    print(sum(abs(x - m) for x in l) // d)


def __starting_point():
    main()

__starting_point()
