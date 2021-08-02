def main():

    D, T, S = map(int, input().split())

    if D / S <= T:
        print("Yes")
    else:
        print("No")


def __starting_point():
    main()


__starting_point()
