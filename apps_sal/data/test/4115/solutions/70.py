def main():
    S = input()
    count = 0
    for i in range(int(len(S) // 2)):
        if(S[i] != S[-i - 1]):
            count += 1
    print(count)


def __starting_point():
    main()


__starting_point()
