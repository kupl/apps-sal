import re


def main():
    input()
    s = re.sub('00+', '0', input().replace(' ', '').strip('0'))
    print(len(s))


def __starting_point():
    main()


__starting_point()
