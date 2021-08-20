import os
import sys


def main():
    L = input()
    if int(L[0]) + int(L[1]) + int(L[2]) + int(L[3]) == 7:
        print('{}+{}+{}+{}=7'.format(L[0], L[1], L[2], L[3]))
    elif int(L[0]) + int(L[1]) + int(L[2]) - int(L[3]) == 7:
        print('{}+{}+{}-{}=7'.format(L[0], L[1], L[2], L[3]))
    elif int(L[0]) + int(L[1]) - int(L[2]) + int(L[3]) == 7:
        print('{}+{}-{}+{}=7'.format(L[0], L[1], L[2], L[3]))
    elif int(L[0]) - int(L[1]) + int(L[2]) + int(L[3]) == 7:
        print('{}-{}+{}+{}=7'.format(L[0], L[1], L[2], L[3]))
    elif int(L[0]) + int(L[1]) - int(L[2]) - int(L[3]) == 7:
        print('{}+{}-{}-{}=7'.format(L[0], L[1], L[2], L[3]))
    elif int(L[0]) - int(L[1]) + int(L[2]) - int(L[3]) == 7:
        print('{}-{}+{}-{}=7'.format(L[0], L[1], L[2], L[3]))
    elif int(L[0]) - int(L[1]) - int(L[2]) + int(L[3]) == 7:
        print('{}-{}-{}+{}=7'.format(L[0], L[1], L[2], L[3]))
    elif int(L[0]) - int(L[1]) - int(L[2]) - int(L[3]) == 7:
        print('{}-{}-{}-{}=7'.format(L[0], L[1], L[2], L[3]))


def __starting_point():
    main()


__starting_point()
