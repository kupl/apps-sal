from collections import Counter
import sys
sys.setrecursionlimit(10 ** 6)
mod = 1000000007
inf = int(1e+18)


def main():
    n = int(input()[-1])
    if n in [2, 4, 5, 7, 9]:
        print('hon')
    elif n in [3]:
        print('bon')
    else:
        print('pon')


main()
