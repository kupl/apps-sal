
def main():
    input()
    s = input()
    one = 0
    zero = 0
    for ch in s:
        if ch == '0':
            one += 1
        else:
            zero += 1

    print(abs(one - zero))


def __starting_point():
    main()


__starting_point()
