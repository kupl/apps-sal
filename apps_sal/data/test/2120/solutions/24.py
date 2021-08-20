def main():
    (n, m) = map(int, input().split())
    vv = list(map(int, input().split()))
    print(sum((min((vv[i - 1] for i in map(int, input().split()))) for _ in range(m))))


def __starting_point():
    main()


__starting_point()
