def main():
    g = []
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    for i in range(n):
        gain = v[i] - c[i]
        if gain > 0:
            g.append(gain)
    print(sum(g))


def __starting_point():
    main()


__starting_point()
