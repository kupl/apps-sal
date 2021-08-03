def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        x = [int(x) for x in input().split()]

        mm = x[0] - 1 + 1
        for i in range(1, k):
            mm = max(mm, 1 + (x[i] - x[i - 1]) // 2)
        mm = max(mm, n - x[-1] + 1)
        print(mm)


def __starting_point():
    main()


__starting_point()
