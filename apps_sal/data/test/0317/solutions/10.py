def Main():
    num = input()
    str = list(input().lower())
    str.sort()
    str = "".join(str)

    for word in range(97, 123):
        symb = chr(word)
        if str.find(symb) == -1:
            print("NO")
            return

    print("YES")
    return


def __starting_point():
    Main()


__starting_point()
