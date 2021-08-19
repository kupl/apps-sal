def generator(x, a):  # xの倍数でaより大きいもののうちの最小値
    if x >= a:
        y = x
    else:
        tmp = a // x + 1
        if a % x == 0:
            tmp -= 1
        y = x * tmp

    return y


def main():
    a, b, x = map(int, input().split())
    minimum = generator(x, a)

    if minimum > b:
        count = 0
    else:
        count = (b - minimum) // x + 1

    if a == 0:
        count += 1

    print(count)


def __starting_point():
    main()


__starting_point()
