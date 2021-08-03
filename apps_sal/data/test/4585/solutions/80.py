def main():
    x = int(input())

    answer = 0
    tmp = 0
    for i in range(10 ** 9):
        tmp += i
        if tmp >= x:
            answer = i
            break

    print(answer)


def __starting_point():
    main()


__starting_point()
