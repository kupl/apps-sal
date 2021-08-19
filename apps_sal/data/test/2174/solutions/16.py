def main():
    n = int(input())
    print(sum((abs(a - b) for (a, b) in zip(sorted(map(int, input().split())), list(range(1, n + 1))))))


def __starting_point():
    main()


__starting_point()
