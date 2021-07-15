def main():
    n, m = list(map(int, input().split()))
    l = [input() for _ in range(n)]
    lead = [[] for _ in range(n)]
    x = 0
    for nn in zip(*l):
        for l, c in zip(lead, nn):
            l.append(c)
        if tuple(l[-1] for l in sorted(lead)) != nn:
            x += 1
            for l in lead:
                del l[-1]
    print(x)


def __starting_point():
    main()

__starting_point()
