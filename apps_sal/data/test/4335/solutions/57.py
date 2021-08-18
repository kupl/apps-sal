def main():
    N = int(input()) // 2
    S = input()

    if S[:N] == S[N:]:
        print("Yes")
    else:
        print("No")


def __starting_point():
    main()


__starting_point()
