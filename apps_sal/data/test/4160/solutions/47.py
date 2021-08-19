def answer(x: int) -> int:
    years = 0
    deposit = 100
    while deposit < x:
        deposit += deposit // 100
        years += 1
    return years


def main():
    x = int(input())
    print(answer(x))


def __starting_point():
    main()


__starting_point()
