import sys


def main():
    n = int(input())
    s = list(map(int, sys.stdin.readline().split()))
    if n % 2 == 1 and s[0] % 2 == 1 and (s[-1] % 2 == 1):
        print('Yes')
    else:
        print('No')


main()
