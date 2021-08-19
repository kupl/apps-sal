#	!/usr/bin/env python3
#	encoding: UTF-8
#	Modified: <15/May/2019 09:06:13 PM>


#	✪ H4WK3yE乡
#	Mohd. Farhan Tahir
#	Indian Institute Of Information Technology (IIIT), Gwalior


import sys


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    s = input().strip()
    ans = [0] * n
    ans[0] = 0
    f = 0
    for i in range(1, n):
        if s[i] == s[i - 1]:
            f = 1 - f
        ans[i] = f

    print(*ans, sep='')


def __starting_point():
    main()


__starting_point()
