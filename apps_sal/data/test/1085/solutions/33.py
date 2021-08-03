def main():
    n = int(input())
    count = 2
    sqrt = int(n ** (1 / 2))
    for i in range(2, sqrt + 1):
        if n % i == 1:
            count += 2
        elif n % i == 0:
            ins = n
            while ins % i == 0:
                ins = ins // i
            if ins % i == 1:
                count += 1
    if sqrt ** 2 == n - 1:
        count -= 1

    print(count)


def __starting_point():
    main()


__starting_point()
