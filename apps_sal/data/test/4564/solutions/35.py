def main():
    s = input()
    answer = 'yes'
    for i in range(len(s) - 1):
        if s[i] in s[i + 1:]:
            answer = 'no'
    print(answer)


def __starting_point():
    main()


__starting_point()
