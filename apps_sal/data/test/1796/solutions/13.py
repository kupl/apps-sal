def main():

    n = int(input())
    sum = 0
    for i in range(n):
        cad = input()
        if cad == "X++" or cad == "++X":
            sum += 1
        else:
            sum -= 1

    print(sum)


def __starting_point():
    main()


__starting_point()
