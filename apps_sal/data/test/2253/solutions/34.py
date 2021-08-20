t = int(input())


def main():
    n = input()
    if n[-1] == 'o':
        print('FILIPINO')
    elif n[-1] == 'u':
        print('JAPANESE')
    elif n[-1] == 'a':
        print('KOREAN')


def __starting_point():
    for i in range(t):
        main()


__starting_point()
