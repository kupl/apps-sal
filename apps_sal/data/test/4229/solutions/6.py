def main() -> None:
    n = int(input())
    answer = 0
    for i in range(1, n + 1):
        if i % 3 != 0 and i % 5 != 0:
            answer += i
    print(answer)
    return


def __starting_point():
    main()


__starting_point()
