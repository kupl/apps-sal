def main():
    s = input()
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        print('Bad')
    else:
        print('Good')


def __starting_point():
    main()


__starting_point()
