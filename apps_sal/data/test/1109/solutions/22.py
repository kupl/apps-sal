def main():
    n, k = map(int, input().split())
    l = input().split()
    print(sum(min(nn.count('1'), nn.count('2')) for nn in zip(*[l[i:i + k] for i in range(0, n, k)])))


def __starting_point():
    main()


__starting_point()
