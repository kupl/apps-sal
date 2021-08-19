def main():
    s = input()
    cnt = s.count('R')
    if cnt == 2 and s[1] != 'R':
        print('1')
    else:
        print(cnt)


def __starting_point():
    main()


__starting_point()
