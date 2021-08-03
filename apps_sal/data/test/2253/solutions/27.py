import math


def main():
    t = int(input())
    for i in range(t):
        sen = str(input())
        if sen.endswith('po'):
            print('FILIPINO')
        elif sen.endswith('desu') or sen.endswith('masu'):
            print('JAPANESE')
        else:
            print('KOREAN')


def __starting_point():
    main()


__starting_point()
