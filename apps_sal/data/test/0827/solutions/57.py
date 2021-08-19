def main():
    n = int(input())
    t = input()
    if t == '1':
        print(2 * 10 ** 10)
        return
    splitted_t = t.split('0')
    if len(splitted_t[0]) > 2 or len(splitted_t[-1]) > 2:
        print(0)
        return
    for sp_ti in splitted_t[1:-1]:
        if len(sp_ti) != 2:
            print(0)
            return
    if splitted_t[-1] == '':
        splitted_t = splitted_t[:-1]
    print(10 ** 10 - len(splitted_t) + 1)


def __starting_point():
    main()


__starting_point()
