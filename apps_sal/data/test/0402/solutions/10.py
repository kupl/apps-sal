def main():
    (n, k) = list(map(int, input().split()))
    t = k
    for i in range(n + 1):
        t += 5 * (i + 1)
        if t > 240:
            print(i)
            return
    print(n)


def __starting_point():
    main()


__starting_point()
