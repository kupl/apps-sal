from collections import Counter
import sys
sys.setrecursionlimit(10 ** 6)
mod = 1000000007
inf = int(1e+18)


def main():
    k = int(input())
    s = input()
    if len(s) > k:
        print(s[:k] + '...')
    else:
        print(s)


main()
