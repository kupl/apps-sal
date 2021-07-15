def main():
    m, t, r = list(map(int, input().split()))
    gh = sorted(map(int, input().split()), reverse=True)
    if r > t:
        print(-1)
        return
    l = [False] * 600
    for g in gh:
        g -= t
        for i in range(g, g + r - sum(l[i] for i in range(g, g + t))):
            l[i] = True
    print(sum(l))


def __starting_point():
    main()

__starting_point()
