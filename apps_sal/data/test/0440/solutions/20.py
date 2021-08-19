def main():
    n = input()
    s = input()
    a = []
    for x in s:
        if x in 'aeiouy':
            if len(a) > 0 and a[-1] in 'aeiouy':
                continue
            else:
                a.append(x)
        else:
            a.append(x)
    print(''.join(a))


def __starting_point():
    main()


__starting_point()
