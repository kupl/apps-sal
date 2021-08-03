def main():
    s = input()
    cc_g = cc_p = 0
    for c in s:
        if c == 'g':
            cc_g += 1
        else:
            cc_p += 1
    print((cc_g - cc_p) // 2)
    return


def __starting_point():
    main()


__starting_point()
